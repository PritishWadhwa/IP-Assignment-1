# Name : PRITISH WADHWA
# Roll No : 2019440
# Group : 1


import datetime
import urllib.request

# JSON is a syntax for storing and exchanging data. 

def getLatestRates():
    """
    Returns: a JSON string that is a response to a latest rates query.

    The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
    """
    url = urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    data = url.read()
    return data


def changeBase(amount, currency, desiredCurrency, date):
    """
    amount is of type int
    currency and desiredCurrency are of type string(INR, USD, etc)
    date is string "yyyy-mm-dd"
    Outputs: returns a float value f.
    """
    newurl = 'https://api.exchangeratesapi.io/' + date
    url = urllib.request.urlopen(newurl)
    data = url.read()
    data = str(data)
    start_desiredCurrency = data.find(desiredCurrency)
    stop_desiredCurrency = data.find(",", start_desiredCurrency + 1)
    value_desiredCurrency = data[start_desiredCurrency + 5:stop_desiredCurrency]
    start_currency = data.find(currency)
    stop_currency = data.find(",", start_currency)
    value_currency = data[start_currency + 5:stop_currency]
    value_desiredCurrency = float(value_desiredCurrency)
    value_currency = float(value_currency)
    value_currency_1 = 1 / value_currency
    value_currency_2 = amount * value_currency_1
    value_final = value_desiredCurrency * value_currency_2
    return value_final


def printAscending(json):
    """
    Output: the sorted order of the Rates
    You don't have to return anything.

    Parameter:
    json: a json string to parse
    """
    value_list = []
    name_list = []
    count_quote = 11
    count_comma = 0
    count_colon = 11
    for i in range(32):
        start_currency = json.find('"', count_quote)
        count_quote = start_currency + 1
        end_currency = json.find('"', count_quote)
        count_quote = end_currency + 1
        currency_name = json[start_currency + 1:end_currency]
        comma_position = json.find(",", count_comma)
        colon_position = json.find(":", count_colon)
        if i == 31:
            currency_value = json[colon_position + 1:comma_position - 1]
        else:
            currency_value = json[colon_position + 1:comma_position]
        currency_value = float(currency_value)
        value_list.append(currency_value)
        name_list.append(currency_name)
        count_comma = comma_position + 2
        count_colon = colon_position + 2
    # sorting
    for i in range(32):
        min_val = i
        for j in range(i + 1, 32):
            if value_list[min_val] > value_list[j]:
                min_val = j
        value_list[i], value_list[min_val] = value_list[min_val], value_list[i]
        name_list[i], name_list[min_val] = name_list[min_val], name_list[i]
    for i in range(32):
        print("1 Euro =  ", end="")
        print(value_list[i], end=" ")
        print(name_list[i])


def extremeFridays(startDate, endDate, currency):
    """
    Output: on which friday was currency the strongest and on which was it the weakest.
    You don't have to return anything.

    Parameters:
    startDate and endDate: strings of the form yyyy-mm-dd
    currency: a string representing the currency those extremes you have to determine
    """
    new_url = "https://api.exchangeratesapi.io/history?start_at=" + startDate + "&end_at=" + endDate
    url = urllib.request.urlopen(new_url)
    data = url.read()
    data_dict = eval(data)
    data_dict_keys = list(data_dict['rates'].keys())
    required_dates = []
    required_value = []
    for i in data_dict_keys:
        date = datetime.datetime(int(i[:4]), int(i[5:7]), int(i[8:]))
        weekday = date.weekday()
        if weekday == 4:
            required_dates.append(i)
            required_value.append(data_dict['rates'][i][currency])
    len_required_value = len(required_value)
    # sorting
    for i in range(len_required_value):
        min_value = i
        for j in range(i + 1, len_required_value):
            if required_value[min_value] > required_value[j]:
                min_value = j
        required_value[i], required_value[min_value] = required_value[min_value], required_value[i]
        required_dates[i], required_dates[min_value] = required_dates[min_value], required_dates[i]
    max_statement = currency + " was strongest on " + required_dates[0] + ". 1 Euro was equal to " + str(required_value[0]) + " " + currency
    min_statement = currency + " was weakest on " + required_dates[len_required_value - 1] + ". 1 Euro was equal to " + str(required_value[len_required_value - 1]) + " " + currency
    print(max_statement)
    print(min_statement)


def findMissingDates(startDate, endDate):
    """
    Output: the dates that are not present when you do a json query from startDate to endDate
    You don't have to return anything.

    Parameters: startDate and endDate: strings of the form yyyy-mm-dd
    both dates are inclusive
    """
    new_url = "https://api.exchangeratesapi.io/history?start_at=" + startDate + "&end_at=" + endDate
    from datetime import date, timedelta
    url = urllib.request.urlopen(new_url)
    data = url.read()
    data_dict = eval(data)
    data_dict_keys = list(data_dict['rates'].keys())
    start_date = datetime.date(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:]))
    end_date = datetime.date(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:]))
    date_difference = end_date - start_date
    date_difference = str(date_difference)
    date_difference_numeric_end = date_difference.find(" ")
    date_difference_numeric = int(date_difference[:date_difference_numeric_end])
    available_dates = []
    date_to_be_added = start_date
    for i in range(date_difference_numeric + 1):
        date_to_be_added_final = str(date_to_be_added)
        available_dates.append(date_to_be_added_final)
        date_to_be_added = date_to_be_added + timedelta(days=1)
    removed_dates = []
    for i in available_dates:
        if i not in data_dict_keys:
            removed_dates.append(i)
    removed_dates.sort()
    print("The following dates were not present:")
    for i in removed_dates:
        print(i[::])

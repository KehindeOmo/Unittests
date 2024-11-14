# symbol: capitalized, 1-7 alpha characters
# chart type: 1 numeric character, 1 or 2
# time series: 1 numeric character, 1 - 4
# start date: date type YYYY-MM-DD
# end date: date type YYYY-MM-DD

#symbol
def testSymbol():
    assert main("GOOGL") == "GOOGL"

def testSymbolLength():
    try:
        main("SEVENORLESS")
    except Exception as e:
        assert str(e) == "Symbol has to have 1 to 7 letters"

def testSymbolCase():
    try:
        main("googl")
    except Exception as e:
        assert str(e) == "Symbol has to be uppercase."

#chart type
def testChartType():
    assert getChartType("1") == 1

def testChartTypev2():
    assert getChartType("2") == 2

def testChartTypeInput():
    try:
        getChartType("3")
    except Exception as e:
        assert str(e) == "Invalid input, only options are 1 or 2."

def testChartTypeNum():
    try:
        getChartType("a")
    except Exception as e:
        assert str(e) == "Invalid input, only numerical values 1 or 2."

#timeseries
def testTimeSeries():
    assert getTimeSeriesFunction("1") == timeSeries["1"]

def testTimeSeriesv2():
    assert getTimeSeriesFunction("2") == timeSeries["2"]

def testTimeSeriesv3():
    assert getTimeSeriesFunction("3") == timeSeries["3"]

def testTimeSeriesv4():
    assert getTimeSeriesFunction("4") == timeSeries["4"]

def testTimeSeriesv5():
    try:
        getTimeSeriesFunction("5")
    except Exception as e:
        assert str(e) == "Invalid input, only options are 1 - 4."

def testTimeSeriesv6():
    try:
        getTimeSeriesFunction("a")
    except Exception as e:
        assert str(e) == "Invalid input, only options are 1 - 4."

#start date
def testStartdate():
    assert validateDate("2024-11-13") == datetime(2024,11,13)


def testStartdatev2():
    try:
        validateDate("13-11-2024")
    except Exception as e:
        assert validateDate("2024-11-13") ==  datetime(2024,11,13)

def testStartdatev3():
    try:
        validateDate("wrong-date-bad")
    except Exception as e:
        assert validateDate("2024-11-13") ==  datetime(2024,11,13)

#end date
def testEnddate():
    assert validateDate("2024-11-13") == datetime(2024,11,13)

def testEnddatev2():
    try:
        validateDate("13-11-2024")
    except Exception as e:
        assert validateDate("2024-11-13") ==  datetime(2024,11,13)
def testEnddatev3():
    try:
        validateDate("wrong-date-bad")
    except Exception as e:
        assert validateDate("2024-11-13") ==  datetime(2024,11,13)


import datetime
import pandas.io.data
import pandas as pd

def getCor(s1_ticker,s2_ticker):

	s1 = pd.io.data.get_data_yahoo(s1_ticker, 
	                                 start=datetime.datetime(1995, 1, 1), 
	                                 end=datetime.datetime(2016, 1, 1))

	s2 = pd.io.data.get_data_yahoo(s2_ticker, 
	                                 start=datetime.datetime(1995, 1, 1), 
	                                 end=datetime.datetime(2016, 1, 1))

	del s1['Open']
	del s1['High']
	del s1['Low']
	del s1['Close']
	del s1['Volume']

	corComp = s1
	corComp.rename(columns={'Adj Close': s1_ticker}, inplace=True)

	corComp[s2_ticker] = s2['Adj Close']

	data = [
		{
			'stock1': s1_ticker,
			'stock2': s2_ticker,
			'20yrCor': round(corComp.tail(5040).corr().values.tolist()[1][0]*100,2),
			'10yrCor': round(corComp.tail(2520).corr().values.tolist()[1][0]*100,2),
			'5yrCor': round(corComp.tail(1260).corr().values.tolist()[1][0]*100,2),
			'2yrCor': round(corComp.tail(504).corr().values.tolist()[1][0]*100,2),
			'1yrCor': round(corComp.tail(252).corr().values.tolist()[1][0]*100,2),
			'6mCor': round(corComp.tail(126).corr().values.tolist()[1][0]*100,2),
			'1mCor': round(corComp.tail(21).corr().values.tolist()[1][0]*100,2),
			'1wCor': round(corComp.tail(5).corr().values.tolist()[1][0]*100,2)
		}
	]

	return data
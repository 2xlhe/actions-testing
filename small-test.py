import pandas

def is_df(df: pandas.DataFrame) -> bool:
    return isinstance(df, pandas.DataFrame)

def is_series(series: pandas.Series) -> bool:
    return isinstance(series, pandas.Series)

def is_index(index: pandas.Index) -> bool:
    return isinstance(index, pandas.Index)

def test_is_df():
    assert is_df(pandas.DataFrame())


df_1 = pandas.DataFrame()
Series_1 = pandas.Series()

test1_result = is_df(df_1)
test2_result = is_df(Series_1)

print(test1_result)
print(test2_result)


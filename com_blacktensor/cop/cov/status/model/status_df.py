import pandas as pd

# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
class CovidStatusDf(object):

    def __init__(self, colums):
        self.colums = colums

    def get_dataframe(self, base_data):
        return pd.DataFrame(base_data, columns=self.colums)
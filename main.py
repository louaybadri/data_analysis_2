import matplotlib.pyplot as plt
import pandas as pd
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm

df = pd.read_excel('Exemple2Reference_SReg.xlsx')

X = df['X']
Y = df['Y']

# X = sm.add_constant(X)

# Fit the linear regression model
# model = sm.OLS(Y, X).fit()

# Obtain the ANOVA table
# anova_table = anova_lm(model)


# Print the ANOVA table
# print(model.model.data.formula)
# print(Y)
# test = pd.DataFrame({'x': X["X"], 'y': Y})
# model2 = sm.OLS(formula='y ~ x', data=test)
print(df)

# model = sm.OLS(Y, X).fit()
# print(model)
model = smf.ols('Y ~ X', data=df).fit()
anova = statsmodels.api.stats.anova_lm(model, typ=2)
# Print the model summary
print(anova)

import pandas as pd
import numpy as np


def expand(X):
    
    
    SCabin = X["Cabin"].apply(spliting_cabin).values.tolist()
    
    
    
    expand_X = {
        "PassengerId" : X["PassengerId"],
        "Pclass" : X["Pclass"],
        "Name" : X["Name"],
        "Sex" : X["Sex"].apply(lambda x: True if x == "female" else False),
        "Age" : X["Age"],
        "SibSp" : X["SibSp"],
        "Parch" : X["Parch"],
        "Ticket" : X["Ticket"],
        "Fare" : X["Fare"],
        "Cabin" : X["Cabin"],
        "Letter" : pd.Series([x[0] for x in SCabin], dtype="category"),
        "Number" : pd.Series([x[1] for x in SCabin]),
        "Many" : pd.Series([x[2] for x in SCabin]),
        "Embarked" : X["Embarked"],
        "Survived" : X["Survived"].astype("bool"),
    }
    
    return pd.DataFrame(expand_X)



def spliting_cabin(x):
    if isinstance(x, float) == True:
        return (None, np.nan, False)
    sx = x.split()
    if len(sx)>1:
        Many = True
    else:
        Many = False
    Letter = sx[0][0]
    if len(sx[0][1:]) == 0:
        Number = np.nan
    else:
        Number = int(sx[0][1:])
    return (Letter, Number, Many)
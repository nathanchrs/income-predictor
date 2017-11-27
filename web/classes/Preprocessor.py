from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn import preprocessing
from sklearn.externals import joblib


class Preprocessor:
    feature_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country']
    discrete_feature_indices = [1, 3, 5, 6, 7, 8, 9, 13]
    discrete_feature_domains = {
        'workclass': ['Private',  'Self-emp-not-inc',  'Self-emp-inc',  'Federal-gov',  'Local-gov',  'State-gov',  'Without-pay',  'Never-worked'],
        'education': ['Bachelors',  'Some-college',  '11th',  'HS-grad',  'Prof-school',  'Assoc-acdm',  'Assoc-voc',  '9th',  '7th-8th',  '12th',  'Masters',  '1st-4th',  '10th',  'Doctorate',  '5th-6th',  'Preschool'],
        'marital-status': ['Married-civ-spouse',  'Divorced',  'Never-married',  'Separated',  'Widowed',  'Married-spouse-absent',  'Married-AF-spouse'],
        'occupation': ['Tech-support',  'Craft-repair',  'Other-service',  'Sales',  'Exec-managerial',  'Prof-specialty',  'Handlers-cleaners',  'Machine-op-inspct',  'Adm-clerical',  'Farming-fishing',  'Transport-moving',  'Priv-house-serv',  'Protective-serv',  'Armed-Forces'],
        'relationship': ['Wife',  'Own-child',  'Husband',  'Not-in-family',  'Other-relative',  'Unmarried'],
        'race': ['White',  'Asian-Pac-Islander',  'Amer-Indian-Eskimo',  'Other',  'Black'],
        'sex': ['Female',  'Male'],
        'native-country': ['United-States',  'Cambodia',  'England',  'Puerto-Rico',  'Canada',  'Germany',  'Outlying-US(Guam-USVI-etc)',  'India',  'Japan',  'Greece',  'South',  'China',  'Cuba',  'Iran',  'Honduras',  'Philippines',  'Italy',  'Poland',  'Jamaica',  'Vietnam',  'Mexico',  'Portugal',  'Ireland',  'France',  'Dominican-Republic',  'Laos',  'Ecuador',  'Taiwan',  'Haiti',  'Columbia',  'Hungary',  'Guatemala',  'Nicaragua',  'Scotland',  'Thailand',  'Yugoslavia',  'El-Salvador',  'Trinadad&Tobago',  'Peru',  'Hong',  'Holand-Netherlands']
    }
    discrete_value_counts = [
        len(discrete_feature_domains['workclass']),
        len(discrete_feature_domains['education']),
        len(discrete_feature_domains['marital-status']),
        len(discrete_feature_domains['occupation']),
        len(discrete_feature_domains['relationship']),
        len(discrete_feature_domains['race']),
        len(discrete_feature_domains['sex']),
        len(discrete_feature_domains['native-country'])
    ]

    def encodeData(self,data):
        features_modes = joblib.load("./model/modes.pkl")
        for c in range(0, len(data)):
            if data[c] == '?':
                data[c] = features_modes[c]

        for c in range(0, len(data)):
          if c in self.discrete_feature_indices:
            domain = self.discrete_feature_domains[self.feature_names[c]]
            data[c] = domain.index(data[c])
        oneHotEncoder = OneHotEncoder(categorical_features=self.discrete_feature_indices, n_values=self.discrete_value_counts)
        
        oneHotEncoder.fit([data])
        data = oneHotEncoder.transform([data]).toarray().astype(int)
        data = data.astype(np.float64)
        data = np.hsplit(data, [-6])

        scaler = joblib.load("./model/scaler.pkl");
        data[1] = scaler.transform(data[1])
        data = np.concatenate(data, axis=1)
        return (data)
      

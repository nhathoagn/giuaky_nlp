from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def one_hot():
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print("Label Encoded:",integer_encoded)

#One-Hot Encoding
onehot_encoder = OneHotEncoder()
onehot_encoded = onehot_encoder.fit_transform(data).toarray()
print("Onehot Encoded Matrix:\n",onehot_encoded)
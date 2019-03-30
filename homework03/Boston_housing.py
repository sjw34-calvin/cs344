from keras.datasets import boston_housing
import pandas
(train_x, train_y), (test_x, test_y) = boston_housing.load_data()


def print_structures():
    print("\n" + "training dimensions:" + "\n" + str(train_x.ndim))
    print("\n" + "training shape:" + "\n" + str(train_x.shape))
    #test images
    # print("\n" + "count:" + "\n" + str(len(test_targets)))
    print("\n" + "test dimensions:" + "\n" + str(test_x.ndim))
    print("\n" + "test shape:" + "\n" + str(test_x.shape))


if __name__ == '__main__':
    print_structures()
    # for a validation set I split the data into 30% validation data and 70% training data below
    validation_data = train_x[:120]
    train_data = train_x[120:]
    # pandas prints the data frame nicely
    dfv = pandas.DataFrame(validation_data)
    dft = pandas.DataFrame(train_data)
    print(dfv)
    print(dft)

    # synthetic feature: I took the property tax and divided it by the per capita crime rate. The goal is to predict the
    # median house value. Therefore, as the crime rate increases, the value of (property tax/crime rate) would decrease
    # thus decreasing median house value.

    train_x_df = pandas.DataFrame(train_x)
    property_tax_per_crime_rate_t = train_x_df[10] / train_x_df[0]
    train_x_df['property_tax_per_crime_rate_t'] = property_tax_per_crime_rate_t

    test_x_df = pandas.DataFrame(test_x)
    property_tax_per_crime_rate_t = test_x_df[10] / test_x_df[0]
    test_x_df['property_tax_per_crime_rate_t'] = property_tax_per_crime_rate_t

    print(train_x_df)
    print(test_x_df)

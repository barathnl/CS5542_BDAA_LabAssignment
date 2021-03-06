from __future__ import print_function

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

# Parameters
learning_rate = 0.01
training_epochs = 1000
display_step = 50

# Training Data
train_X = numpy.asarray([
    6.575,6.421,7.185,6.998,7.147,6.43,6.012,6.172,5.631,6.004,6.377,6.009,5.889,5.949,6.096,5.834,5.935,5.99,5.456,5.727,5.57,
    5.965,6.142,5.813,5.924,5.599,5.813,6.047,6.495,6.674,5.713,6.072,5.95,5.701,6.096,5.933,5.841,5.85,5.966,6.595,7.024,6.77,
    6.169,6.211,6.069,5.682,5.786,6.03,5.399,5.602,5.963,6.115,6.511,5.998,5.888,7.249,6.383,6.816,6.145,5.927,5.741,5.966,6.456,
    6.762,7.104,6.29,5.787,5.878,5.594,5.885,6.417,5.961,6.065,6.245,6.273,6.286,6.279,6.14,6.232,5.874,6.727,6.619,6.302,6.167,
    6.389,6.63,6.015,6.121,7.007,7.079,6.417,6.405,6.442,6.211,6.249,6.625,6.163,8.069,7.82,7.416,6.727,6.781,6.405,6.137,6.167,
    5.851,5.836,6.127,6.474,6.229,6.195,6.715,5.913,6.092,6.254,5.928,6.176,6.021,5.872,5.731,5.87,6.004,5.961,5.856,5.879,5.986,
    5.613,5.693,6.431,5.637,6.458,6.326,6.372,5.822,5.757,6.335,5.942,6.454,5.857,6.151,6.174,5.019,5.403,5.468,4.903,6.13,5.628,
    4.926,5.186,5.597,6.122,5.404,5.012,5.709,6.129,6.152,5.272,6.943,6.066,6.51,6.25,7.489,7.802,8.375,5.854,6.101,7.929,5.877,
    6.319,6.402,5.875,5.88,5.572,6.416,5.859,6.546,6.02,6.315,6.86,6.98,7.765,6.144,7.155,6.563,5.604,6.153,7.831,6.782,6.556,
    7.185,6.951,6.739,7.178,6.8,6.604,7.875,7.287,7.107,7.274,6.975
])

train_Y = numpy.asarray([
    4.09,4.9671,4.9671,6.0622,6.0622,6.0622,5.5605,5.9505,6.0821,6.5921,6.3467,6.2267,5.4509,4.7075,4.4619,4.4986,4.4986,4.2579,
    3.7965,3.7965,3.7979,4.0123,3.9769,4.0952,4.3996,4.4546,4.682,4.4534,4.4547,4.239,4.233,4.175,3.99,3.7872,3.7598,3.3603,3.3779,
    3.9342,3.8473,5.4011,5.4011,5.7209,5.7209,5.7209,5.7209,5.1004,5.1004,5.6894,5.87,6.0877,6.8147,6.8147,6.8147,6.8147,7.3197,
    8.6966,9.1876,8.3248,7.8148,6.932,7.2254,6.8185,7.2255,7.9809,9.2229,6.6115,6.6115,6.498,6.498,6.498,5.2873,5.2873,5.2873,
    5.2873,4.2515,4.5026,4.0522,4.0905,5.0141,4.5026,5.4007,5.4007,5.4007,5.4007,4.7794,4.4377,4.4272,3.7476,3.4217,3.4145,3.0923,
    3.0921,3.6659,3.6659,3.615,3.4952,3.4952,3.4952,3.4952,3.4952,2.7778,2.8561,2.7147,2.7147,2.421,2.1069,2.211,2.1224,2.4329,
    2.5451,2.7778,2.6775,2.3534,2.548,2.2565,2.4631,2.7301,2.7474,2.4775,2.7592,2.2577,2.1974,2.0869,1.9444,2.0063,1.9929,1.7572,
    1.7883,1.8125,1.9799,2.1185,2.271,2.3274,2.4699,2.346,2.1107,1.9669,1.8498,1.6686,1.6687,1.6119,1.4394,1.3216,1.4118,1.3459,
    1.4191,1.5166,1.4608,1.5296,1.5257,1.618,1.5916,1.6102,1.6232,1.7494,1.7455,1.7364,1.8773,1.7573,1.7659,1.7984,1.9709,2.0407,
    2.162,2.422,2.2834,2.0459,2.4259,2.1,2.2625,2.4259,2.3887,2.5961,2.6463,2.7019,3.1323,3.5549,3.3175,2.9153,2.829,2.741,2.5979,
    2.7006,2.847,2.9879,3.2797,3.1992,3.7886,4.5667,4.5667,6.4798,6.4798,6.4798,6.2196,6.2196,5.6484,7.309,7.309,7.309,7.6534,
])
n_samples = train_X.shape[0]

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')

    # Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    # Testing example, as requested (Issue #2)
    test_X = numpy.asarray([
        7.135,6.162,7.61,7.853,8.034,5.891,6.326,5.783,6.064,5.344,5.96,5.404,5.807,
        6.375,5.412,6.182,5.888,6.642,5.951,6.373,6.951,6.164,6.879,6.618,8.266, 8.725,
        8.04,7.163,7.686,6.552,5.981,7.412,8.337,8.247,6.726,6.086,6.631,7.358,6.481,
        6.606,6.897,6.095,6.358,6.393,5.593,5.605,6.108,6.226,6.433,6.718
    ])
    test_Y = numpy.asarray([
        7.6534,6.271,6.271,5.118,5.118,3.9454,4.3549,4.3549,4.2392,3.875,3.8771,3.665,
        3.6526,3.9454,3.5875,3.9454,3.1121,3.4211,2.8893,3.3633,2.8617,3.048,3.2721,
        3.2721,2.8944,2.8944,3.2157,3.2157,3.3751,3.3751,3.6715,3.6715,3.8384,3.6519,
        3.6519,3.6519,4.148,4.148,6.1899,6.1899,6.3361,6.3361,7.0355,7.0355,7.9549,7.9549,
        8.0555,8.0555,7.8265,7.8265
    ])

    print("Testing... (Mean square loss Comparison)")
    testing_cost = sess.run(
        tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * test_X.shape[0]),
        feed_dict={X: test_X, Y: test_Y})  # same function as cost above
    print("Testing cost=", testing_cost)
    print("Absolute mean square loss difference:", abs(
        training_cost - testing_cost))

    plt.plot(test_X, test_Y, 'bo', label='Testing data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
plt.show()
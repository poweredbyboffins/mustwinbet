import neurolab as nl

# Logical &
input = [[0.6, 0.3,0.3], [0.7, 0.4,0.2], [0.2, 0.8,0.1], [0.2, 0.6,0.2]]
target = [[1], [1], [0], [0]]

# Create net with 2 inputs and 1 neuron
net = nl.net.newp([[0, 1],[0,1],[0,1]],1)

# train with delta rule
# see net.trainf
error = net.train(input, target, epochs=100, show=10, lr=0.1)
test = [[0.2,0.7,0.1]]
out = net.sim(test)
print(out)

# Plot results
import pylab as pl
#pl.plot(error)
pl.plot(out)
pl.xlabel('Epoch number')
pl.ylabel('Train error')
pl.grid()
pl.show()

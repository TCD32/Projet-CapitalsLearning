import matplotlib.pyplot as plt

def plot_training_analysis(history, accuracyType):
  #acc = history.history['sparse_categorical_accuracy']
  #acc = history.history['accuracy']
  acc = history.history[accuracyType]
  val_acc = history.history['val_'+accuracyType]
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs = range(len(acc))

  plt.plot(epochs, acc, 'b', linestyle="--",label='Training acc')
  plt.plot(epochs, val_acc, 'g', label='Validation acc')
  plt.title('Training and validation accuracy')
  plt.legend()

  plt.figure()

  plt.plot(epochs, loss, 'b', linestyle="--",label='Training loss')
  plt.plot(epochs, val_loss,'g', label='Validation loss')
  plt.title('Training and validation loss')
  plt.legend()

  plt.show()
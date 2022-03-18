import numpy as np
import pickle
from apscheduler.schedulers.background import BackgroundScheduler

horizon = 24 # how far to predict forward
window_size = 24 # how far to lookback

def multivariate_multistep_data(X, y, window_size, horizon):
    data = []
    labels = []
    for i in range(window_size, len(X)-horizon):
      data.append(X[i-window_size:i])
      labels.append(y[i:i+horizon])

    return np.array(data), np.array(labels)

def data_preprocessing():
  pass

def data
def main(args):
    # asyncio.get_event_loop().run_until_complete(start_all_users_async())
    scheduler = BackgroundScheduler(timezone='Asia/Ho_Chi_Minh')
    scheduler.add_job(update_trade_history,'interval', minutes=10)
    scheduler.start()
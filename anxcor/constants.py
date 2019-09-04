"""
defaults used in processing routine initialization
"""
TAPER_DEFAULT   =0.05
RESAMPLE_DEFAULT=10.0
UPPER_CUTOFF_FREQ=5.0
LOWER_CUTOFF_FREQ=0.01
MAX_TAU_DEFAULT=100.0
FILTER_ORDER_BANDPASS=4
SECONDS_2_NANOSECONDS = 1e9
OPERATIONS_SEPARATION_CHARACTER = '->:'

## t-norm constants
T_NORM_TYPE='reduce_metric'
T_NORM_ROLLING_METRIC= 'mean'
T_NORM_REDUCE_METRIC = 'max'
T_NORM_WINDOW=10.0
T_NORM_LOWER_FREQ=0.001
T_NORM_UPPER_FREQ=0.05

## Whitening constants
WHITEN_REDUCE_METRIC = None
WHITEN_ROLLING_METRIC='mean'
WHITEN_WINDOW_RATIO=0.01
FILTER_ORDER_WHITEN=3
WHITEN_TYPE='reduce_metric'
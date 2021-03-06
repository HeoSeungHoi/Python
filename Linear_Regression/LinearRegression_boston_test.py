from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

boston = load_boston()
# boston 객체 리턴
print(boston.DESCR)
print(type(boston.DESCR))
print("boston.data.shape :", boston.data.shape, " type :", type(boston.data))
# boston.data.shape : (506, 13)  type : <class 'numpy.ndarray'>

print("boston.target.shape :", boston.target.shape)  # 보스턴 전체 데이터는 506개
# boston.target.shape : (506,)


# Training Data/Test Data 나누기
# 일반적으로 주어진 데이터에 80%는 학습용 20%는 테스트용으로 사용
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=0)  # 데이터 분할
print(X_train.shape)  # train 데이터로 379개
# (379, 13)

print(X_train)
# [[1.9133e-01 2.2000e+01 5.8600e+00 ... 1.9100e+01 3.8913e+02 1.8460e+01]
#  [1.0328e-01 2.5000e+01 5.1300e+00 ... 1.9700e+01 3.9690e+02 9.2200e+00]
#  [1.0469e-01 4.0000e+01 6.4100e+00 ... 1.7600e+01 3.8925e+02 6.0500e+00]
#  ...
#  [1.5098e-01 0.0000e+00 1.0010e+01 ... 1.7800e+01 3.9451e+02 1.0300e+01]
#  [2.2927e-01 0.0000e+00 6.9100e+00 ... 1.7900e+01 3.9274e+02 1.8800e+01]
#  [1.3914e-01 0.0000e+00 4.0500e+00 ... 1.6600e+01 3.9690e+02 1.4690e+01]]


print(X_test.shape)  # test 데이터로 127개
# (127, 13)

print(X_test)
# [[6.7240e-02 0.0000e+00 3.2400e+00 ... 1.6900e+01 3.7521e+02 7.3400e+00]
#  [9.2323e+00 0.0000e+00 1.8100e+01 ... 2.0200e+01 3.6615e+02 9.5300e+00]
#  [1.1425e-01 0.0000e+00 1.3890e+01 ... 1.6400e+01 3.9374e+02 1.0500e+01]
#  ...
#  [3.4940e-01 0.0000e+00 9.9000e+00 ... 1.8400e+01 3.9624e+02 9.9700e+00]
#  [9.8490e-02 0.0000e+00 2.5650e+01 ... 1.9100e+01 3.7938e+02 1.7580e+01]
#  [7.5030e-02 3.3000e+01 2.1800e+00 ... 1.8400e+01 3.9690e+02 6.4700e+00]]

# 선형 회귀 분석 수해하기
model_boston = LinearRegression().fit(X_train, y_train)  # 선형회귀분석 모델 생성 후 바로 트레이닝 까지
print(" model_boston.coef_ :", model_boston.coef_)
#  model_boston.coef_ : [-1.16869578e-01  4.39939421e-02 -5.34808462e-03  2.39455391e+00
#  -1.56298371e+01  3.76145473e+00 -6.95007160e-03 -1.43520477e+00
#   2.39755946e-01 -1.12937318e-02 -9.86626289e-01  8.55687565e-03
#  -5.00029440e-01]

print("model_boston.intercept_ :", model_boston.intercept_)
# model_boston.intercept_ : 36.98045533762074

predictions = model_boston.predict(X_test)
print(predictions)
# [24.95242095 23.62103603 29.21341544 11.97586964 21.33688522 19.47270023
#  20.42304705 21.52151744 18.99420776 19.91486748  4.93479475 16.05522458
#  16.91865924  5.34748135 39.8532679  32.33300268 22.33140869 36.54399797
#  31.03481174 23.32519523 24.92272042 24.26965237 20.71353663 30.45335016
#  22.45699529  9.87018454 17.70327024 17.96092462 35.69651424 20.79470104
#  18.10460338 17.6798399  19.71471124 23.80071994 29.06967938 19.22845092
#  10.9827218  24.56507125 17.29284531 15.18639065 26.10224841 20.87956585
#  22.26213357 15.32658621 22.85990998 25.0946293  19.74938589 22.69795393
#   9.66269908 24.46020219 20.69146192 17.51925862 24.45743226 30.094858
#  13.30018094 21.51999888 20.66106358 15.34165143 13.77778277 22.07762378
#  17.53500273 21.60779414 32.91070817 31.32857473 17.65125782 32.70348085
#  18.55078395 19.31741597 18.78727742 23.04648674 22.82036456 24.00303326
#  30.63350586 28.86342332 25.78494589  5.01083121 36.82552503 23.8068372
#  27.37235786 19.33065964 28.51578786 19.19074039 18.82054011 37.93522185
#  39.33322173 23.90917632 24.9637454  15.66636329 25.91938239 16.55998182
#  15.76062081 12.84804532 24.44579694 30.93489709 22.37344054 20.1771727
#   0.23188403 25.26750166 15.30346141 17.79919916 25.44719906 22.46545062
#  32.57935565 22.01736145 27.37282281 23.31791564  6.27801893 14.75380843
#  22.45283857 29.11140243 32.97991193 12.84146396 19.79934244 20.59548927
#  12.06242669 23.3859831   4.70107176 19.83644906  9.17601554 44.63193984
#  30.63472777 12.29476892 17.54228223 21.5013417  23.63874649 20.28667337
#  35.17503496]

# 테스트 데이터에 대한 예측 수행하기

# 평가....
print("훈련 세트 점수 : ", model_boston.score(X_train, y_train))
# 훈련 데이터 세트 점수 :  0.7697448370563938

# 테스트 데이터와 테스트 목표 값을 넣어주면, 예측 값을 만들어 비교 해 준다. --> R2 스코어
# 함수 내부에 기울기 값과 절편값이 다 들어있기 때문에 결과 생성 가능
print("테스트 세트 점수 : ", model_boston.score(X_test, y_test)) 
# 테스트 데이터 세트 점수 :  0.6353620786674621

#실측값과 테스트 데이터의 결과를 넣어주면 R2 스코어 계산 
print("R2_score : ", r2_score(y_test, predictions)) # 결과 값이 1 일경우 완전 똑같은 것
# R2_score :  0.6353620786674621

mse = mean_squared_error(y_test, predictions)
print("mse :", mse)
# mse : 29.790559164238505

# get_error(y_test, predictions)
plt.scatter(y_test, predictions)
plt.xlabel(" Real Boston House Price")
plt.ylabel(" Predict Boston House Price")
plt.show()

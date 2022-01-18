# Title     : TODO
# Objective : TODO

sin(pi)         # 1.224606e-16
log(3)          # 1.098612 (자연로그)
log10(100)      # 2  (상용로그)
floor(3.14)     # 3  (버림)
ceiling(5.87)   # 6  (올림)
round(4.65)     # 5  (반올림)

# 그래프 예제
# load some data
data(mtcars)
# create a basic scatterplot
plot(mtcars$wt, mtcars$mpg)
# specify better axis labels and add a title
plot(mtcars$wt, mtcars$mpg, xlab="Weight", ylab="Miles per gallon", main="Weight vs. Miles per Gallon")

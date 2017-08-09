msp_times <- read.csv("/times_matrix.csv",header = FALSE)
fit <- cmdscale(msp_times, eig = TRUE, k = 2)
write.csv(fit$points,file = "/Users/carstonhernke/PycharmProjects/geodata/fitted_coordinates_mpls.csv")
#fit
#x <- fit$points[,1]
#y <- fit$points[,2]

#rbGrad <- colorRampPalette(c('red','yellow','green'))
#colors <- rbGrad(10)[1:64]
#plot(x, y, pch = 19, xlim = range(x) + c(0, 20),col = rbGrad(64))
#x <- 0 - x
#y <- 0 - y
#plot(x, y, pch = 19, xlim = range(x) + c(0, 600))
#text(x, y, pos = 4, labels = city.names)



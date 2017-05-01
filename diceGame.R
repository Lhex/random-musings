library(ggplot2)

diceRoll <- function() {
  numbers <- c(1:6)
  sample(numbers, 1, replace = TRUE)
}

getPlotData <- function(n = 5000) {
  max_length <- 1
  max_height <- 1
  mid_X <- max_length/2
  mid_Y <- max_height/2
  X <- 0.5
  Y <- 0.5
  
  plot_data <- data.frame(X = X, Y = Y, roll = 0)
  
  # plot <- ggplot() +
  #   geom_point(data = plot_data, aes(x = X, y = Y))
  # plot
  
  i <- 0
  while(i < n) {
    roll <- diceRoll()
    if (roll < 3) {
      Y <- (Y + max_height) / 2
      X <- (X + mid_X) / 2
    } else if (roll > 4) {
      X <- (X + max_length) / 2
      Y <- Y / 2
    } else {
      X <- X / 2
      Y <- Y / 2
    }
    
    plot_data <- rbind(plot_data, data.frame(X = X, Y = Y, roll = roll))
    
    i <- i + 1
  } 
  plot_data$roll <- as.factor(plot_data$roll)
  
  plot <- ggplot(data = plot_data) +
    geom_point(aes(x = X, y = Y, color = roll), size = 0.5) +
    xlim(0,max_length) +
    ylim(0,max_height)
  plot
}

PlotChaos <- function(plot_data) {
  
}

## Apendix

## Wrong formula giving slanted shape
# while(i < 5000) {
#   roll <- diceRoll()
#   if (roll < 3) {
#     Y <- (Y + max_height) / 2
#     X <- (X + mid_X) / 2
#   } else if (roll > 4) {
#     X <- (X + max_length) / 2
#     Y <- (Y + mid_Y) / 2
#   } else {
#     X <- X / 2
#     Y <- Y / 2
#   }
#   
#   plot_data <- rbind(plot_data, data.frame(X = X, Y = Y, roll = roll))
#   
#   i <- i + 1
# } 
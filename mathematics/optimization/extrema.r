library(tidyverse)
library(plotly)

# Example Function
dat <- data.frame(x=c(1,2,3,4,5), y=c(1,2,3,4,5), z=c(1,2,3,2,1))
model <- lm(z~x+y+I(x^2) + I(y^2), data=dat)
hp_disp_grid <- expand_grid(x=seq(1,5, by=1), y=seq(1,5, by=1))
grid <- hp_disp_grid %>% mutate(pred = predict(model, newdata=data.frame(x,y)))
grid_wide <- grid %>% pivot_wider(names_from=x, values_from=pred) %>% select(-1) %>% as.matrix()
fig <- plot_ly(dat, x=~x, y=~y, z=~z, type="scatter3d")
fig2 <- add_trace(p=fig, z=grid_wide, x=seq(1,5,by=1), y=seq(1,5, by=1), type="surface")
# Find extrema
max_val <- which(grid_wide == max(grid_wide), arr.ind=TRUE)
min_val <- which(grid_wide == min(grid_wide), arr.ind=TRUE)

max_val_df <- as.data.frame(max_val)
max_cords <- data.frame(x=(max_val_df$col), y=(max_val_df$row))
max_val_pred <- predict(model, max_cords)

min_val_df <- as.data.frame(min_val)
min_cords <- data.frame(x=(min_val_df$col), y=(min_val_df$row))
min_val_pred <- predict(model, min_cords)

# Plot the extrema
max_cords$pred <- max_val_pred
min_cords$pred <- min_val_pred

fig3 <- add_trace(p=fig2, x=max_cords$x, y=max_cords$y, z=max_cords$pred, type="scatter3d", name="Maximum Values")
fig4 <- add_trace(p=fig3, x=min_cords$x, y=min_cords$y, z=min_cords$pred, type="scatter3d", name="Minimum Values")
fig4

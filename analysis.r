library(tidyverse)

df <- read_csv("./data/rankings/brown_rankings_1_10.csv")
# Let's change the column names
n_days <- ncol(df) - 1
col_headers = map_chr(seq(1, n_days), str_glue)
col_headers <- c("word", col_headers)

colnames(df) <- col_headers

df_long <- df |>
    pivot_longer(c("1":"10"), names_to="day", values_to="rank") |>
    mutate(day = factor(day))


rank_by_day <- function(day_id) {
    df_long |> filter(day == day_id) |> arrange(rank) |> select(c(word, rank))
}

library(tidyverse)
library(lubridate)
library(rvest)
library(glue)


dl_month <- function(month = 'january') {
  url <- glue("https://nationaltoday.com/{month}-holidays/")
  pg <- url %>% 
    read_html()
}

parse_month <- function(pg) {
  pat <- "#archive-date .date , .title, #archive-date .date"
  pg %>% 
    html_nodes(pat) %>% 
    html_text() %>% 
    split(c('date','text')) %>% 
    as_tibble() %>% 
    slice(2:nrow(.)) %>% 
    mutate(date = str_squish(date)) %>% 
    mutate(date_frm = as.Date(date, format = "%a %b %d"))
}

# parse_month(dl_month('february'))

month(1:12, label = T, abbr = F) %>% 
  tolower() -> mos

pages <- map(mos, dl_month)
# save(pages, file = 'national_day_html.rData')
# load('national_day_html.rData')

map(pages, parse_month) %>% 
  bind_rows() %>% 
  filter(!is.na(date_frm)) -> national_days


write_csv(national_days, 'national_days.csv')


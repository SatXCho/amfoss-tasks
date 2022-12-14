use std::fs::File;
use std::io::prelude::*;
extern crate reqwest;
extern crate scraper;




fn main() {


    let response = reqwest::blocking::get(
        "https://crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();

    let mut file = File::create("out.csv")
    .expect("no file");

    
    //name
    let document = scraper::Html::parse_document(&response);
    let crypto_name_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let cryptoname = document.select(&crypto_name_selector).map(|x| x.inner_html());

    cryptoname
        .zip(1..51)
        .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    //price
    let crypto_price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let cryptoprice = document.select(&crypto_price_selector).map(|x| x.inner_html());

    cryptoprice
        .zip(1..51)
        .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    //css-1b7j986
    //change
    let crypto_change_selector = scraper::Selector::parse("td.css-1b7j986>p").unwrap();
    let cryptochange = document.select(&crypto_change_selector).map(|x| x.inner_html());

    cryptochange
        .zip(1..51)
        .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });
    
    //css-1nh9lk8
    //volume
    let crypto_volume_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let cryptovolume = document.select(&crypto_volume_selector).map(|x| x.inner_html());

    cryptovolume
        .zip(1..51)
        .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    //css-1nh9lk8
    //cap
    let crypto_cap_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let cryptocap = document.select(&crypto_cap_selector).map(|x| x.inner_html());

    cryptocap
        .zip(1..51)
        .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    


}

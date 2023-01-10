//use std::fs::File;
use std::error::Error;
//use std::io;
use itertools::izip;
extern crate reqwest;
extern crate scraper;
extern crate csv;



fn main() -> Result<(), Box<dyn Error>> {


    let response = reqwest::blocking::get(
        "https://crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();

    
    //name
    let document = scraper::Html::parse_document(&response);
    let crypto_name_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let cryptoname = document.select(&crypto_name_selector).map(|x| x.inner_html());

    // cryptoname
    //     .zip(1..51);
    //     .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    //price
    let crypto_price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let cryptoprice = document.select(&crypto_price_selector).map(|x| x.inner_html());

    // cryptoprice
    //     .zip(1..51)
    //     .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    //css-1b7j986
    //change
    let crypto_change_selector = scraper::Selector::parse("td.css-1b7j986>p").unwrap();
    let cryptochange = document.select(&crypto_change_selector).map(|x| x.inner_html());

    // cryptochange
    //     .zip(1..51)
    //     .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });
    
    //css-1nh9lk8
    //volume
    let crypto_volume_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let cryptovolume = document.select(&crypto_volume_selector).map(|x| x.inner_html());

    // cryptovolume
    //     .zip(1..51)
    //     .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    //css-1nh9lk8
    //cap
    let crypto_cap_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let cryptocap = document.select(&crypto_cap_selector).map(|x| x.inner_html());

    // cryptocap
    //     .zip(1..51)
    //     .for_each(|(item, number)| { file.write_all(item.as_bytes()).expect("no"); });

    let crypto_data = izip!(cryptoname, cryptoprice, cryptochange, cryptovolume, cryptocap);

    let mut writer = csv::Writer::from_path("crypto.csv")?;
    for (name, price, change, volume, cap) in crypto_data {
        let record = vec![name.to_string(), price.to_string(), change.to_string(), volume.to_string(), cap.to_string()];
        writer.write_record(record)?;
    }
    writer.flush()?;


    Ok(())
}

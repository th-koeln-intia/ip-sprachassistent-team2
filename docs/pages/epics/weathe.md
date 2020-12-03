---
# This top area is to give jekyll information about the page.
layout: page
permalink: /epics/weather/
title: Weather-service on Rhasspy
---

## Goals

We want to ask Heimdal for the current or future weather, maybe also for a forcast for tomorrow or during the next week 
at our current location. In addition it would be nice to ask for the current weather and forecast in other places.

## Weather-API
For our weather API the same basic criteria apply as for our other technologies, it should be DSGVO conform, free of charge,
or even open-source. Of course the service should give us reliable data. In the following we looked at Accuweather (Accu], Dark Sky (DS),
Deutscher Wetterdienst (DWD) and openweathermap(OWM).

### Comparrison

| Criteria      |Weight | Accu  | DS    | DWD   | OWM   |
|---------------|:-----:|:-----:|:-----:|:-----:|:-----:|       
| Privacie      | 4     | X     | X     | 10    | 8     |
| Opensource    | 1     | 0     | 0     | 0     | 3     |
| free of charge| 2     | 0     | X     | 10    | 8     |
| Usability     | 3     | X     | X     | 4     | 7     |
| Total         |       | 0     | 0     | 24    | 26    |

We gave each criteria a weight witch we use to multiple our "educated guesses" for points with. The sum of each providers
points times the weight factor is the Basis of our Criteria. We used X if we did not find information about a given criteria
or the Provider did not match a critical one like, basic privacy or being available free of charge.

#### About open-source

There are open standardised weather algorithms and most weather stations publish there data in one way or another. Most 
providers use these algorithms to prepare and redistribute and redistribute the data. But there codebase itself is usually not 
public. But we want to give points for good business practices and  

#### [accuweather](https://www.accuweather.com/)

Accuweather is not free and the pricing structure is not transparent. We would need to request prices from there sales 
department. 

#### [Dark Skies](darksky.net)

Dark Sky got aquiered by Apple in March 2020.

> Dark Sky said its API service, which allows other apps to use its weather data, will no longer accept new signups and 
> will continue to function through the end of 2021. Several other weather apps rely on Dark Sky’s data, which means 
> they’ll have to find another source.

[CNBC](https://www.cnbc.com/2020/03/31/apple-buys-popular-weather-app-dark-sky.html)

Because their data will no longer be publicly available outside the Apple eco system the missed the critical criteria of
being publicly available and free of charge.

#### [Deutscher Wetterdienst (dwd)](https://www.dwd.de/DE/derdwd/derdwd_node.html)

> The Deutscher Wetterdienst is a public institution with partial legal capacity under the Federal Ministry of Transport
> and Digital Infrastructure.

DWD provides meteorological data and research to the economy and society.
DWD only offers their data as ziped files and there is no API to access it. But there is a
[pallet](https://flows.nodered.org/node/node-red-contrib-dwd-local-weather) in node-red, that provides
data from DWD. [List of weather stations](https://www.dwd.de/DE/leistungen/met_verfahren_mosmix/mosmix_stationskatalog.cfg?view=nasPublication&nn=16102)

#### [openweathermap.org](https://openweathermap.org/)

Requiers registration, free plan for up to 60 calls per minute. (600 calls per minute for 40$ per month)

Has an node Red pallet, that offers current weather and a 5 day forecast, current, future and historical weather data awailable in JSON

On [openweathermap.org](https://openweathermap.org/find?q=) we can search for our location or city and enter the name and
two character country code into the node, to get the local weather data. This is also dynamicly possible via a function node
but not jet implemented.

## Implementation


## request weather data as global

Saving Weatherdata as Globals since openweathermap


### Intents

First we want to implement the intends GetWeather and an Intent GetWeatherWithLocation or GetWaetherLocation. We add the
following sentences to sentences.ini in the Rhasspy web application. Later we want to implement a weather forecast as well

```
[GetWeather]
wie ist das wetter

[GetWeatherInLocation]
wie ist das wetter in (Stadt){city}
```

### Add ID to the Payload


## Open Questions

1. How will users set there location?

    Setting location depending on ID
    Extracting City from users command.

2. How do we handle weekdays?

    Different Intends?
3. How do we handel expressions like "this afternoon | evening"

## Sources

[cstain.io](https://cstan.io/?p=12097&lang=en)

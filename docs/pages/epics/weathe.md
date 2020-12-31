---
# This top area is to give jekyll information about the page.
layout: page
permalink: /epics/weather/
title: Weather-service on Rhasspy
---

## Goals

We want to ask Heimdal for the current or future weather, maybe tomorrow or the during the next week for our current
location. In addition it would be nice to ask for weather in other places

## Weather-API
For our weather API the same basic criteria apply as for our other technologies, it should be DSGVO conform, free of charge,
or even open-source. Of course the service should give us reliable data. In the following we looked at Accuweather, Dark Skies,
Deutscher Wetterdienst and openweathermap.

### Comparrison

#### [accuweather](https://www.accuweather.com/)

Is not free. We would need to request prices from there sales department.

#### [Dark Skies](https://darksky.net/)
Dark Skies was bought by Apple. They will be IOS and MacOS exclusive and stop providing data over their API in 2021.



#### [Deutscher Wetterdienst (dwd)](https://www.dwd.de/DE/derdwd/derdwd_node.html)

> The Deutscher Wetterdienst is a public institution with partial legal capacity under the Federal Ministry of Transport
and Digital Infrastructure.

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


### Intends

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

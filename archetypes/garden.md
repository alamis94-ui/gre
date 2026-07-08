---
slug: "{{ substr (sha256 now) 0 10 }}"
type: garden
title: {{ title (replaceRE `[-_]` " " .Name) }}
latlon: [ 0, 0 ]
author: Author Name
translator: Translator Name
contributor: Contributor Name
date: {{ time.Now.Format "2006-01-02" }}
draft: true
---

## Dates


<!--
## Excavation Dates
-->

## Garden Description


<!--
## Maps
{{< image file="filename.jpg" caption="" credit="" alt="" >}}
-->

<!--
## Plans
{{< image file="filename.jpg" caption="" credit="" alt="" >}}
-->

<!--
## Images
{{< image file="filename.jpg" caption="" credit="" alt="" >}}
-->

<!--
## Bibliography

- BIB_ENTRY [(worldcat)](WORLDCAT_LINK_URL)
-->

<!--
## Keywords

- {{< keyword "example" >}}
-->

<!--
## Places

- {{< id vocab="Pleiades" id="" name="" >}}
- {{< id vocab="TGN" id="" name="" >}}
-->

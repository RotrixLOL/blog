---
title: "Theme guide for myself"
date: 2022-12-09T15:49:55+01:00
categories: ["Hugo"]
tags: ["Guide", "theme"]
---

## Kinda quotes

{{<lead>}}
When life gives you lemons, make lemonade.
{{</lead>}}

## Alerts

{{<alert>}}
**This is important:** Look!
{{</alert>}}

## Badges
Take a look at this cool badge:
{{<badge>}}
Test Badge!
{{</badge>}}

## Buttons

Here you have kinda a button:

{{<button href="#button" target="_self">}}
Cool button
{{</button>}}

## Charts

The charts are difficult!
{{<chart>}}
type: 'bar',
data: {
  labels: ['RotrixX', 'Tesla', 'Twitter', 'Elon Musk'],
  datasets: [{
    label: 'quantity of $',
    data: [89129804, 6023813, 3012946, 9832718]
  }]
}
{{</chart>}}
Just look at that!

## Icons

Here you have some cool icons:

{{<icon "facebook">}}
{{<icon "github">}}
{{<icon "twitter">}}
[{{<icon "dev">}}](https://dev.to/rotrixx)

## Lists

**A list:**

{{< list limit=3 >}}

## Colors

Showcase of colors:
{{< swatches "#e4e4e4" "#6bf" "#9fb" >}}

{{< swatches "#eee" "#2bf" "#4bd" >}}

## Diagrams

### Not very basic diagram:

{{<mermaid>}}
graph LR;
A[Learn]-->B[Code];
B-->C[Profit]
{{</mermaid>}}

### Other one:
{{<mermaid>}}
gantt
dateFormat DD-MM-YYYY
title GANTT diagram

section A section
Completed task :done des1, 01-01-2022, 18-04-2022
Active task :active des2, 18-04-2022, 30-08-2022
Future task : des3, 30-08-2022, 09-04-2023

{{</mermaid>}}

### Some git graph:
{{<mermaid>}}
gitGraph
  commit tag: "v1.0.0"
  commit
  branch nightly
  commit tag: "v1.1.0"
  commit
  commit
  checkout main
  commit tag: "v1.0.1"
  commit
  merge nightly
  commit tag: "v1.2.0"
  commit
{{</mermaid>}}

## Thanks for reading :)

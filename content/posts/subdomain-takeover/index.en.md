---
title: "Subdomain Takeover: how an atacker can take control of your website"
date: 2023-05-01T13:46:15Z
description: "Take preventive measures to protect your website from subdomain takeover. Learn how to monitor your subdomains, properly configure DNS records, and use detection tools to prevent malicious attacks. Find out how to protect your website against subdomain takeover in this article."
---

Computer attacks are increasingly sophisticated and, in many cases, they can go unnoticed for a long time. One of these types of attacks is subdomain takeover, in which an attacker can take control of a subdomain of a website and use it for its own malicious purposes. In this article, we will explore what the subdomain takeover is, how you work and how you can protect your website against it.

## What is subdomain takeover?

The vulnerable records are the **_CNAME_**, which are the ones that point to another domain.

Let's give an example. Imagine that you are hosting your project at Github Pages or in some other similar service. You decide that you want a personalized domain, for example: `project.example.com` that points to `user.github.io/project`. So far everything is fine.

But one day you decide to delete your account, and if someone tries to access your project, he will not be able to do it. Now an attacker can create a Github account with the name you had and use your personalized subdomain to host your own malicious website. If a user tries to access your project, it will be redirected to the attacker's website without even realizing it. This could lead to the phishing, if the page you were staying was a login and the attacker clone that page redirecting the credentials to its database, for example.

## How the subdomain takeover works

This type of attack is known as subdomain takeover and can have serious consequences for your website and your users. The attacker can use your subdomain to house phishing, malware, or any other malicious content, which can damage your reputation and put the safety of your users at risk.

It is important to keep in mind that the example we mention is only one of the scenarios in which a subdomain takeover can occur. There are many other ways in which an attacker can take advantage of a vulnerable subdomain, such as when a third -party service is no longer available and the subdomain is no longer in use.

Therefore, it is essential that websites owners take measures to protect against this type of attack. Here are some preventive measures that can be taken to avoid a subdomain takeover:

## How to protect your website against subdomain takeover

1. **Monitor the subdomains**: It is important to have a list of all the subdomains used on the website and regularly monitor their status and activity to detect any suspicious change. It is also advisable to monitor inactive subdomains or that are no longer used and deactivated or eliminated if necessary.

2. **Correctly configure DNS records**: DNS records are a fundamental part of the configuration of a website and must be configured correctly to avoid possible vulnerabilities.

3. **Use detection tools**: There are several tools available online that can help detect possible subdomain takeovers, such as [takeover](https://github.com/m4ll0k/takeover). This tool can scan your domain to see if there are free subdomains.

## Conclusions

In conclusion, subdomain takeover is a real risk for any website, and attackers can take advantage of it in various ways. However, there are measures that you can take to detect and prevent this type of attack. It is important to be aware of the threat and take measures to protect your website and your users. Regularly monitor subdomains, correctly configure DNS records and use detection tools are some of the best practices to protect your website against subdomain takeover.

Thanks for your reading!

---
title: "Intro to RCEs: What they are and how to prevent them"
date: 2023-05-02T21:28:09Z
description: "An RCE (Remote Code Execution) allows the attacker to execute malicious code on a remote server if, for example, you have a website with a vulnerable parameter in the url. Discover more about RCEs and how to prevent them in this article!"
summary: "An RCE (Remote Code Execution) allows the attacker to execute malicious code on a remote server if, for example, you have a website with a vulnerable parameter in the url. Discover more about RCEs and how to prevent them in this article!"
categories: ["Hacking"]
tags: ["RCE"]
---
The RCE (Remote Code Execution) are very easy to write as a developer, and commonly easy to exploit as an attacker. If you want to understand what they are, how they work and how we can prevent them as developers, keep reading this article, you will surely learn!

## What is a RCE?

A RCE is a vulnerability that allows an attacker to execute malicious code in a remote system, usually on a website.

This means that if you have a web application housed on your own server, an attacker could take advantage of a parameter in the URL to inject code. This allows the attacker to get possible access to the server.

## How does a RCE work?

Imagine that you are hosting a PHP online store on your server and you have a parameter for the functionality of the pagination. Well, an attacker could try a variety of combinations to inject commands.

This type of vulnerability is present in many [HTB](https://hackthebox.com) machines so you should master it. The best way? Practice, the more you explode this vulnerability, the easier it will be.

`http://www.example.com/index.php?page=;whoami`

In this case, the attacker is using the **Command Injection** technique to execute the _whoami_ command to see with which user the app is being executed.

## How to prevent a RCE?

To prevent a RCE, it is essential to follow good practices. Here are some measures that can be taken to prevent the RCE:

### Update the software

Keeping updated software at all times is crucial to ensure that known vulnerabilities are corrected. This includes the operating system, web applications and any service that is executed in the system.

### Validate and sanitize entry

It is important to validate all the user input that is received through the web application to ensure that malicious data is not introduced. This may include the validation of the entrance length, the elimination of special characters and the validation of data types. In addition, entry sanitization refers to the elimination of malicious or dangerous characters from the user input. This may include the elimination of special characters and input coding to avoid code injection.

### Configure the server safely

Setting the server safe is essential to avoid the RCE. This includes the deactivation of unnecessary services, the use of safe passwords and the implementation of firewall and other security mechanisms.

And although shell can be obtained, it is also important to complicate the privilege escalation as a security measure, so that the attacker gets access, that he cannot do much.

### Perform security tests

Perform regular security tests in the web application and on the server is important to detect any security vulnerability. This may include penetration tests and vulnerabilities analysis, although as a developer you can also try to inject code.

## Conclusion

The RCE is a serious threat to the security that can allow an attacker to take complete control of a remote system. To prevent it, it is essential to keep updated software, validate and sanitize the user input, configure the server safely and perform regular safety tests. By following these best security practices, we can significantly reduce the risk of RCE and protect our systems and data against malicious attacks.

Thanks for reading!

{{< alert >}}
Soon I will write HTB writeups and web development posts!
{{< /alert >}}

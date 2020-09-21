<img src="https://img.unocero.com/2019/03/javascript.jpg">

# 0x13. Javascript - Objects, Scopes and Closures

Object basics
An object is a collection of related data and/or functionality (which usually consists of several variables and functions — which are called properties and methods when they are inside objects.) Let's work through an example to understand what they look like.

To begin with, make a local copy of our oojs.html file. This contains very little — a <script> element for us to write our source code into. We'll use this as a basis for exploring basic object syntax. While working with this example you should have your developer tools JavaScript console open and ready to type in some commands.

What is "this"?
You may have noticed something slightly strange in our methods. Look at this one for example:

greeting: function() {
  alert('Hi! I\'m ' + this.name.first + '.');
}
You are probably wondering what "this" is. The this keyword refers to the current object the code is being written inside — so in this case this is equivalent to person. So why not just write person instead? As you'll see in the Object-oriented JavaScript for beginners article, when we start creating constructors and so on, this is very useful — it always ensures that the correct values are used when a member's context changes (for example, two different person object instances may have different names, but we want to use their own name when saying their greeting).

Let's illustrate what we mean with a simplified pair of person objects:

const person1 = {
  name: 'Chris',
  greeting: function() {
    alert('Hi! I\'m ' + this.name + '.');
  }
}

const person2 = {
  name: 'Deepti',
  greeting: function() {
    alert('Hi! I\'m ' + this.name + '.');
  }
}
In this case, person1.greeting() outputs "Hi! I'm Chris."; person2.greeting() on the other hand outputs "Hi! I'm Deepti.", even though the method's code is exactly the same in each case. As we said earlier, this is equal to the object the code is inside — this isn't hugely useful when you are writing out object literals by hand, but it really comes into its own when you are dynamically generating objects (for example using constructors). It will all become clearer later on.

A prototype-based language?
JavaScript is often described as a prototype-based language — to provide inheritance, objects can have a prototype object, which acts as a template object that it inherits methods and properties from.

An object's prototype object may also have a prototype object, which it inherits methods and properties from, and so on. This is often referred to as a prototype chain, and explains why different objects have properties and methods defined on other objects available to them.

In JavaScript, a link is made between the object instance and its prototype (its __proto__ property, which is derived from the prototype property on the constructor), and the properties and methods are found by walking up the chain of prototypes.

---

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)


---

## Installation

Copy the code, compile (if is necessary), and execute it.

---

### Setup

---

## Features
## Usage

See the codes of different functions and programs.

## Documentation

<a href="https://intranet.hbtn.io/rltoken/OJ4pU6uHwfCrAclbZsk_Hg">`JavaScript object basics`</a><br>
<a href="https://intranet.hbtn.io/rltoken/Uqv-UMsBUpHWQZXBf5fn0g">`Object-oriented JavaScript`</a><br>
<a href="https://intranet.hbtn.io/rltoken/zMWxOmGWEsOCldCKeDswCA">`Class - ES6`</a><br>
<a href="https://intranet.hbtn.io/rltoken/DTMKogwFYEgUnpLrNvTcfQ">`super - ES6`</a><br>
<a href="https://intranet.hbtn.io/rltoken/fh2JHfNNa-HLnmfSdOo9TA">`extends - ES6`</a><br>
<a href="https://intranet.hbtn.io/rltoken/lrlwnQMM82RimJJcfLao5w">`Object prototypes`</a><br>
<a href="https://intranet.hbtn.io/rltoken/LDpXxzBrdmmXAHoNrWwLxg">`Inheritance in JavaScript`</a><br>
<a href="https://intranet.hbtn.io/rltoken/qDa7F8060Jlhe3DZZitY4A">`Closures`</a><br>
<a href="https://intranet.hbtn.io/rltoken/ockP7FQKKmTRvfeAHw-XSw">`this/self`</a><br>
<a href="https://intranet.hbtn.io/rltoken/22mdHf9KeFhRQrLP-e1hPw">`Modern JS`</a><br>

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using.
---

## Team

https://github.com/Charliemur2
---

## Support

Feel free to contact me!

- GitHub at <a href="https://github.com/Charliemur2">`Charliemur2`</a>
- Twitter at <a href="https://twitter.com/charliesoka">`@charliesoka`</a>
- Insert more social links here.

---

## License

Free Source Code

<!-- omit in toc -->
# ICE-ATIS models

![Python package](https://github.com/egillanton/ice-atis-nlu-models/workflows/Python%20package/badge.svg)

<!-- omit in toc -->
## Table of Contents

<details>
<summary>Click to expand</summary>

- [1. Introduciton](#1-introduciton)
- [2. Setup](#2-setup)
	- [2.1. Create a virtual environment](#21-create-a-virtual-environment)
	- [2.2. Activate virtual environment](#22-activate-virtual-environment)
	- [2.3. Install dependecies](#23-install-dependecies)
	- [2.4. Set evironment variable](#24-set-evironment-variable)
	- [2.5. Run setup.sh](#25-run-setupsh)
- [3. Example of Usage](#3-example-of-usage)
- [4. Contributors](#4-contributors)
</details>


## 1. Introduciton

This repository contains the scrips and pretrained models trained on the [ICE-ATIS](https://github.com/egillanton/ice-atis) dataset.

## 2. Setup

<details>
<summary>Click to expand</summary>

### 2.1. Create a virtual environment

```console
$ python3 -m venv venv
```

### 2.2. Activate virtual environment

```console
$ . ./venv/Scripts/activate
```

### 2.3. Install dependecies

```console
(venv)$ pip install -r requirements.txt
```

### 2.4. Set evironment variable

```console
(venv)$ export PYTHONPATH=src
```

### 2.5. Run setup.sh

This will optain the ICE-ATIS dataset and place it in the root directory.

```console
(venv)$ . setup.sh
```
</details>

## 3. Example of Usage

```python
from utils.get_data import load_model, get_most_common_label

trigram_model = load_model("models/ngram.trigram.pickle")
trigram_test_tokens = ('til', 'boston', 'frá')
trigram_test_label = get_most_common_label(trigram_test_tokens, trigram) # B-toloc.city_name
```

## 4. Contributors
<a href="https://github.com/egillanton/ice-atis-nlu-models/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=egillanton/ice-atis-nlu-models" />
</a>
<!-- Made with [contributors-img](https://contributors-img.web.app). -->

[Become a contributor](CONTRIBUTING.md)

<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>


# coin
Simple Coin module, Just Flip!

![coin](https://user-images.githubusercontent.com/50411472/139525970-2868d0ec-a158-4d03-b1a6-f0a3e180d46a.png)


## Desctiption

*coin* is a module that only helps generate random numbers between 0 and 1.

It's simple and easy to use.


## Dependencies

*coin* is self-contained. The module has no dependencies


## Test & Installation

1. Test
```console
$ make test
```
2. Installation
```console
$ make
$ pip3 install dist/[module name].whl
```


## Usage

```python
from coin import coin

new_coin = coin.Coin()
print(new_coin.flip())
# 0 or 1

new_coin.set_side(1)
print(new_coin.get_side())
# 1
```

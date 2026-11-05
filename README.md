# shop-demo

A tiny shop library used to demonstrate the Autonomous Bug-Fixing Agent.

It ships with two known bugs (see the open issues). The existing tests pass today because they only cover the
happy paths, so the agent has to write its own reproduction before it can prove a fix.

```
pip install -r requirements.txt
python -m pytest
```

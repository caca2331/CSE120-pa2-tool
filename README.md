## usage:
python timespread.py <the result of your program>
To generate the result of your program:
for thread i (0 <= i <= 9):
 - Whenever you enter a process i, DPrint "si" (for example, "s1")
 - SlowPrintf the "iiiiiiiiiiiiiiii" (the more the better)
 - Whenever you exit a process i, DPrint "ei"

Make your tab size to 8 for a good-looking format.

## sample code:
```
  void Main()
  {
    if (Fork() == 0) {
      DPrintf("s2");
      RequestCPUrate(30);
      SlowPrintf(3, "2222222222");
      DPrintf("e2");
      Exit();
    }
    DPrintf("s1");
    RequestCPUrate(70);
    SlowPrintf(3, "1111111111");
    DPrintf("e1");
    Exit();
  }
```
## sample output string:
s11s221121121112112e122222e2

## sameple script output:
### Make your tab size to 8 for a good-looking format.
```
0	1	2	3	4	5	6	7	8	9
entering p1, 0chars printed
10.0	10.0	10.0	10.0	10.0	10.0	10.0	10.0	10.0	10.0
entering p2, 1chars printed
0.0	100.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
exiting  p1, 14chars printed
0.0	64.29	35.71	0.0	0.0	0.0	0.0	0.0	0.0	0.0
exiting  p2, 5chars printed
0.0	0.0	100.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
```

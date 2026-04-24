### Valid 1
```plaintext
let p = T
let q = F
let r = (NOT ((NOT p) AND q))
if r then print p
```

### Valid 2
```plaintext
let p = T
print p
```

### Valid 3
```plaintext
let p = T
let q = F
let r = (p AND q)
print r
```

### Valid 4
```plaintext
let p = T
let a = (NOT p)
if a then print p
```

### Valid 5
```plaintext
let p = T
let q = F
let x = ((p OR q) AND p)
print x
```

### Valid 6
```plaintext
let p = T
let q = F
let x = ((p OR q) IMPLIES (NOT q))
print x
```

### Valid 7
```plaintext
let p = T
let q = F
let r = T
let s = F
let x = (((p AND q) OR r) IMPLIES (NOT s))
print x
```

### Valid 8
```plaintext
let p = T
let q = F
let r = T
let x = (((p AND (NOT q)) OR (NOT (NOT r))) IMPLIES ((NOT p) OR r))
print x
```

### Valid 9
```plaintext
let p = T
let q = T
let r = F
if p then if q then print r
```

### Valid 10
```plaintext
let p = F
if T then print p
```

### Valid 11
```plaintext
let a = T
let b = F
let c = T
let d = F
let e = T
let x = ((((a OR b) OR c) OR d) OR e)
print x
```

### Valid 12
```plaintext
let x = T
let x = F
let x = (NOT x)
print x
```

### Valid 13
```plaintext
let p = T
let q = F
if p then print q
```

### Valid 14
```plaintext
let p = T
let q = T
let x = (p AND q)
print x
```

### Valid 15
```plaintext
let p = F
let q = F
let x = (p OR q)
print x
```

### Valid 16
```plaintext
let p = T
let q = F
let x = (p IMPLIES q)
print x
```

### Valid 17
```plaintext
let p = F
let x = (NOT p)
print x
```

### Valid 18
```plaintext
let p = T
let q = F
let r = T
let x = ((p AND q) OR r)
print x
```

### Valid 19
```plaintext
let p = T
let q = F
let r = F
let x = ((p OR q) AND (NOT r))
print x
```

### Valid 20
```plaintext
let p = T
let q = F
let r = T
let x = ((p IMPLIES q) OR r)
print x
```

### Valid 21
```plaintext
let p = F
let q = T
let r = F
let x = ((p OR q) IMPLIES r)
print x
```

### Valid 22
```plaintext
let p = T
let q = T
if (p AND q) then print p
```

### Valid 23
```plaintext
let p = T
let q = F
if (p OR q) then let r = (NOT q)
```

### Valid 24
```plaintext
let p = T
let q = F
let r = T
if (p IMPLIES q) then print r
```

### Valid 25
```plaintext
let p = T
let q = F
let r = T
if (NOT q) then if r then print p
```

### Valid 26
```plaintext
let p = T
let q = F
let x = ((NOT p) OR (NOT q))
print x
```

### Valid 27
```plaintext
let p = T
let q = F
let r = T
let s = F
let x = (((p AND r) OR (q AND s)) IMPLIES (p OR s))
print x
```

### Valid 28
```plaintext
let a = T
let b = T
let c = F
let x = ((a AND b) IMPLIES (b OR c))
print x
```

### Valid 29
```plaintext
let p = T
let q = F
let r = T
let x = (NOT ((p AND q) OR (NOT r)))
print x
```

### Valid 30
```plaintext
let p = T
let q = F
let r = T
let s = F
let t = T
let x = ((((p OR q) AND (r OR s)) IMPLIES t) OR (NOT q))
print x
```

### Valid 31
```plaintext
let p = T
let q = F
let r = T
let x = ((p AND (NOT q)) IMPLIES (r OR q))
print x
```

### Valid 32
```plaintext
let p = T
let q = F
let r = T
let s = T
let x = (((p IMPLIES q) IMPLIES r) AND s)
print x
```

### Valid 33
```plaintext
let p = T
let q = T
let r = F
let x = ((p AND (NOT r)) OR (q AND r))
print x
```

### Valid 34
```plaintext
let p = T
let x = (p AND T)
print x
```

### Valid 35
```plaintext
let p = F
let x = (F OR p)
print x
```

### Valid 36
```plaintext
let p = T
let x = (p AND F)
print x
```

### Valid 37
```plaintext
let p = F
let x = (p OR T)
print x
```

### Valid 38
```plaintext
let p = T
let x = (p AND p)
print x
```

### Valid 39
```plaintext
let p = T
let x = (p OR p)
print x
```

### Valid 40
```plaintext
let p = T
let x = (p AND (NOT p))
print x
```

### Valid 41
```plaintext
let p = T
let x = (p OR (NOT p))
print x
```

### Valid 42
```plaintext
let p = T
let q = F
let x = (p AND (p OR q))
print x
```

### Valid 43
```plaintext
let p = T
let q = F
let x = (p OR (p AND q))
print x
```

### Valid 44
```plaintext
let x = (NOT T)
print x
```

### Valid 45
```plaintext
let x = (NOT F)
print x
```

### Valid 46
```plaintext
let p = T
let x = (NOT (NOT p))
print x
```

### Valid 47
```plaintext
let p = T
let q = F
let x = (NOT (p AND q))
print x
```

### Valid 48
```plaintext
let p = T
let q = F
let x = (NOT (p OR q))
print x
```

### Valid 49
```plaintext
let p = T
let q = F
let x = ((p AND q) OR p)
print x
```

### Valid 50
```plaintext
let p = T
let q = F
let r = T
let s = F
let t = T
let u = F
let x = (NOT (((((p AND (NOT q)) OR (r AND (NOT s))) IMPLIES (t OR u)) AND (NOT (p IMPLIES r)))))
print x
```

### Valid 51
```plaintext
let a = T
let b = F
let c = T
let d = F
let e = T
let f = F
if (((a AND (NOT b)) OR ((c IMPLIES d) AND (NOT (e OR f)))) IMPLIES (a OR c)) then print a
```

### Valid 52
```plaintext
let p = T
let q = F
let r = T
let s = F
if (NOT ((NOT ((p OR q) IMPLIES (r AND (NOT s)))) AND (p IMPLIES (q OR r)))) then let x = (NOT (p AND s))
```

## Invalid - Error Cases

### Lexical Errors

### Invalid L1
```plaintext
assign p = T
```

### Invalid L2
```plaintext
let P = T
```

### Invalid L3
```plaintext
let pp = T
```

### Invalid L4
```plaintext
let x = (p and q)
```

### Invalid L5
```plaintext
let p := T
```

### Invalid L6
```plaintext
let x = (p XOR q)
```

### Syntax Errors

### Invalid S1
```plaintext
let p = T
if (p AND ) then print p
```

### Invalid S2
```plaintext
let x = (p AND)
```

### Invalid S3
```plaintext
let x = (AND p q)
```

### Invalid S4
```plaintext
if p print q
```

### Invalid S5
```plaintext
let p =
```

### Invalid S6
```plaintext
print (p AND q)
```

### Invalid S7
```plaintext
let x = (p AND q) IMPLIES r
```

### Invalid S8
```plaintext
let x = ((p AND q)
```

### Invalid S9
```plaintext
let x = (p AND q))
```

### Invalid S10
```plaintext
let x = ()
```

### Invalid S11
```plaintext
let x = (p)
```

### Invalid S12
```plaintext
let x = ((p))
```

### Invalid S13
```plaintext
if p then if q print r
```

### Invalid S14
```plaintext
if p then then q
```

### Invalid S15
```plaintext
if then print p
```

### Invalid S16
```plaintext
let p (NOT q)
```

### Invalid S17
```plaintext
let x = p AND q
```

### Invalid S18
```plaintext
let x = (AND OR NOT)
```

### Execution Errors

### Invalid E1
```plaintext
let p = t
```

### Invalid E2
```plaintext
let x = (p AND q)
print x
```

### Invalid E3
```plaintext
let x = (x AND T)
```

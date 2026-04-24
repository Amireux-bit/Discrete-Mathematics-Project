### Valid 1
```plaintext
let p = T
let q = F
let r = (NOT ((NOT p) AND q))
if r then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "IF",
        "VAR_R",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        [
          "NOT",
          [
            "AND",
            [
              "NOT",
              "VAR_P"
            ],
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        "VAR_R",
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        [
          "OR",
          "VAR_P",
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        "VAR_R",
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 2
```plaintext
let p = T
print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE"
    },
    "printed_output": [
      {
        "line": 2,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 3
```plaintext
let p = T
let q = F
let r = (p AND q)
print r
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_R"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_R"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_R"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "FALSE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 4
```plaintext
let p = T
let a = (NOT p)
if a then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_A",
        "EQ",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "IF",
        "VAR_A",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_A",
        [
          "NOT",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        "VAR_A",
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_A",
        [
          "NOT",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        "VAR_A",
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_A": "FALSE"
    },
    "printed_output": []
  }
}
```

### Valid 5
```plaintext
let p = T
let q = F
let x = ((p OR q) AND p)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "AND",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ],
          "VAR_P"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 6
```plaintext
let p = T
let q = F
let x = ((p OR q) IMPLIES (NOT q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_S",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "OR",
        "VAR_R",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "NOT",
        "VAR_S",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "OR",
            [
              "AND",
              "VAR_P",
              "VAR_Q"
            ],
            "VAR_R"
          ],
          [
            "NOT",
            "VAR_S"
          ]
        ]
      ]
    },
    {
      "line": 6,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            [
              "OR",
              [
                "NOT",
                "VAR_P"
              ],
              [
                "NOT",
                "VAR_Q"
              ]
            ],
            [
              "NOT",
              "VAR_R"
            ]
          ],
          [
            "NOT",
            "VAR_S"
          ]
        ]
      ]
    },
    {
      "line": 6,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 5,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R",
          "VAR_S"
        ],
        "ast_original_column": [
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_S": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 6,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 8
```plaintext
let p = T
let q = F
let r = T
let x = (((p AND (NOT q)) OR (NOT (NOT r))) IMPLIES ((NOT p) OR r))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "NOT",
        "VAR_R",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN",
        "OR",
        "VAR_R",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "OR",
            [
              "AND",
              "VAR_P",
              [
                "NOT",
                "VAR_Q"
              ]
            ],
            [
              "NOT",
              [
                "NOT",
                "VAR_R"
              ]
            ]
          ],
          [
            "OR",
            [
              "NOT",
              "VAR_P"
            ],
            "VAR_R"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            [
              "OR",
              [
                "NOT",
                "VAR_P"
              ],
              "VAR_Q"
            ],
            [
              "NOT",
              "VAR_R"
            ]
          ],
          [
            "OR",
            [
              "NOT",
              "VAR_P"
            ],
            "VAR_R"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 9
```plaintext
let p = T
let q = T
let r = F
if p then if q then print r
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "IF",
        "VAR_P",
        "THEN",
        "IF",
        "VAR_Q",
        "THEN",
        "PRINT",
        "VAR_R"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        "VAR_P",
        [
          "IF",
          "VAR_Q",
          [
            "PRINT",
            "VAR_R"
          ]
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        "VAR_P",
        [
          "IF",
          "VAR_Q",
          [
            "PRINT",
            "VAR_R"
          ]
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "TRUE",
      "VAR_R": "FALSE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 10
```plaintext
let p = F
if T then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "IF",
        "TRUE",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "IF",
        "TRUE",
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "IF",
        "TRUE",
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "FALSE"
    },
    "printed_output": [
      {
        "line": 2,
        "output": "FALSE"
      }
    ]
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_A",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_B",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_C",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_D",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_E",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_A",
        "OR",
        "VAR_B",
        "R_PAREN",
        "OR",
        "VAR_C",
        "R_PAREN",
        "OR",
        "VAR_D",
        "R_PAREN",
        "OR",
        "VAR_E",
        "R_PAREN"
      ]
    },
    {
      "line": 7,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_A",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_B",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_C",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_D",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_E",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "OR",
            [
              "OR",
              [
                "OR",
                "VAR_A",
                "VAR_B"
              ],
              "VAR_C"
            ],
            "VAR_D"
          ],
          "VAR_E"
        ]
      ]
    },
    {
      "line": 7,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_A",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_B",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_C",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_D",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_E",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "OR",
            [
              "OR",
              [
                "OR",
                "VAR_A",
                "VAR_B"
              ],
              "VAR_C"
            ],
            "VAR_D"
          ],
          "VAR_E"
        ]
      ]
    },
    {
      "line": 7,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_A": "TRUE",
      "VAR_B": "FALSE",
      "VAR_C": "TRUE",
      "VAR_D": "FALSE",
      "VAR_E": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 7,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 12
```plaintext
let x = T
let x = F
let x = (NOT x)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "VAR_X",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "VAR_X"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "VAR_X"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 13
```plaintext
let p = T
let q = F
if p then print q
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "IF",
        "VAR_P",
        "THEN",
        "PRINT",
        "VAR_Q"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        "VAR_P",
        [
          "PRINT",
          "VAR_Q"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        "VAR_P",
        [
          "PRINT",
          "VAR_Q"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 14
```plaintext
let p = T
let q = T
let x = (p AND q)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 15
```plaintext
let p = F
let q = F
let x = (p OR q)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "FALSE",
      "VAR_Q": "FALSE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 16
```plaintext
let p = T
let q = F
let x = (p IMPLIES q)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "IMPLIES",
        "VAR_Q",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "NOT",
            "VAR_P"
          ],
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 17
```plaintext
let p = F
let x = (NOT p)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 18
```plaintext
let p = T
let q = F
let r = T
let x = ((p AND q) OR r)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "OR",
        "VAR_R",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            "VAR_P",
            "VAR_Q"
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            "VAR_P",
            "VAR_Q"
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 19
```plaintext
let p = T
let q = F
let r = F
let x = ((p OR q) AND (NOT r))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_R",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ],
          [
            "NOT",
            "VAR_R"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ],
          [
            "NOT",
            "VAR_R"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 20
```plaintext
let p = T
let q = F
let r = T
let x = ((p IMPLIES q) OR r)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "IMPLIES",
        "VAR_Q",
        "R_PAREN",
        "OR",
        "VAR_R",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "IMPLIES",
            "VAR_P",
            "VAR_Q"
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "OR",
            [
              "NOT",
              "VAR_P"
            ],
            "VAR_Q"
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 21
```plaintext
let p = F
let q = T
let r = F
let x = ((p OR q) IMPLIES r)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "IMPLIES",
        "VAR_R",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            [
              "NOT",
              "VAR_P"
            ],
            [
              "NOT",
              "VAR_Q"
            ]
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "FALSE",
      "VAR_Q": "TRUE",
      "VAR_R": "FALSE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 22
```plaintext
let p = T
let q = T
if (p AND q) then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "IF",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ],
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ],
        [
          "PRINT",
          "VAR_P"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 23
```plaintext
let p = T
let q = F
if (p OR q) then let r = (NOT q)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "IF",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "THEN",
        "LET",
        "VAR_R",
        "EQ",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        [
          "OR",
          "VAR_P",
          "VAR_Q"
        ],
        [
          "LET",
          "VAR_R",
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "IF",
        [
          "OR",
          "VAR_P",
          "VAR_Q"
        ],
        [
          "LET",
          "VAR_R",
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE"
    },
    "printed_output": []
  }
}
```

### Valid 24
```plaintext
let p = T
let q = F
let r = T
if (p IMPLIES q) then print r
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "IF",
        "L_PAREN",
        "VAR_P",
        "IMPLIES",
        "VAR_Q",
        "R_PAREN",
        "THEN",
        "PRINT",
        "VAR_R"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        [
          "IMPLIES",
          "VAR_P",
          "VAR_Q"
        ],
        [
          "PRINT",
          "VAR_R"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        [
          "OR",
          [
            "NOT",
            "VAR_P"
          ],
          "VAR_Q"
        ],
        [
          "PRINT",
          "VAR_R"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE"
    },
    "printed_output": []
  }
}
```

### Valid 25
```plaintext
let p = T
let q = F
let r = T
if (NOT q) then if r then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "IF",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "THEN",
        "IF",
        "VAR_R",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        [
          "NOT",
          "VAR_Q"
        ],
        [
          "IF",
          "VAR_R",
          [
            "PRINT",
            "VAR_P"
          ]
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "IF",
        [
          "NOT",
          "VAR_Q"
        ],
        [
          "IF",
          "VAR_R",
          [
            "PRINT",
            "VAR_P"
          ]
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 26
```plaintext
let p = T
let q = F
let x = ((NOT p) OR (NOT q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "NOT",
            "VAR_P"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "NOT",
            "VAR_P"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_S",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_R",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "VAR_Q",
        "AND",
        "VAR_S",
        "R_PAREN",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_S",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "OR",
            [
              "AND",
              "VAR_P",
              "VAR_R"
            ],
            [
              "AND",
              "VAR_Q",
              "VAR_S"
            ]
          ],
          [
            "OR",
            "VAR_P",
            "VAR_S"
          ]
        ]
      ]
    },
    {
      "line": 6,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            [
              "OR",
              [
                "NOT",
                "VAR_P"
              ],
              [
                "NOT",
                "VAR_R"
              ]
            ],
            [
              "OR",
              [
                "NOT",
                "VAR_Q"
              ],
              [
                "NOT",
                "VAR_S"
              ]
            ]
          ],
          [
            "OR",
            "VAR_P",
            "VAR_S"
          ]
        ]
      ]
    },
    {
      "line": 6,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 5,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R",
          "VAR_S"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_S": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 6,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 28
```plaintext
let a = T
let b = T
let c = F
let x = ((a AND b) IMPLIES (b OR c))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_A",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_B",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_C",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_A",
        "AND",
        "VAR_B",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "VAR_B",
        "OR",
        "VAR_C",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_A",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_B",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_C",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "AND",
            "VAR_A",
            "VAR_B"
          ],
          [
            "OR",
            "VAR_B",
            "VAR_C"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_A",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_B",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_C",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "OR",
            [
              "NOT",
              "VAR_A"
            ],
            [
              "NOT",
              "VAR_B"
            ]
          ],
          [
            "OR",
            "VAR_B",
            "VAR_C"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_A",
          "VAR_B",
          "VAR_C"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_A": "TRUE",
      "VAR_B": "TRUE",
      "VAR_C": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 29
```plaintext
let p = T
let q = F
let r = T
let x = (NOT ((p AND q) OR (NOT r)))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "NOT",
        "VAR_R",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          [
            "OR",
            [
              "AND",
              "VAR_P",
              "VAR_Q"
            ],
            [
              "NOT",
              "VAR_R"
            ]
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "OR",
            [
              "NOT",
              "VAR_P"
            ],
            [
              "NOT",
              "VAR_Q"
            ]
          ],
          "VAR_R"
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R"
        ],
        "ast_original_column": [
          "FALSE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_S",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_T",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "AND",
        "L_PAREN",
        "VAR_R",
        "OR",
        "VAR_S",
        "R_PAREN",
        "R_PAREN",
        "IMPLIES",
        "VAR_T",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 7,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_T",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "IMPLIES",
            [
              "AND",
              [
                "OR",
                "VAR_P",
                "VAR_Q"
              ],
              [
                "OR",
                "VAR_R",
                "VAR_S"
              ]
            ],
            "VAR_T"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 7,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_T",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "OR",
            [
              "OR",
              [
                "AND",
                [
                  "NOT",
                  "VAR_P"
                ],
                [
                  "NOT",
                  "VAR_Q"
                ]
              ],
              [
                "AND",
                [
                  "NOT",
                  "VAR_R"
                ],
                [
                  "NOT",
                  "VAR_S"
                ]
              ]
            ],
            "VAR_T"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 7,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 6,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R",
          "VAR_S",
          "VAR_T"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_S": "FALSE",
      "VAR_T": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 7,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 31
```plaintext
let p = T
let q = F
let r = T
let x = ((p AND (NOT q)) IMPLIES (r OR q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "VAR_R",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "IMPLIES",
          [
            "AND",
            "VAR_P",
            [
              "NOT",
              "VAR_Q"
            ]
          ],
          [
            "OR",
            "VAR_R",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "OR",
            [
              "NOT",
              "VAR_P"
            ],
            "VAR_Q"
          ],
          [
            "OR",
            "VAR_R",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 4,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_S",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "IMPLIES",
        "VAR_Q",
        "R_PAREN",
        "IMPLIES",
        "VAR_R",
        "R_PAREN",
        "AND",
        "VAR_S",
        "R_PAREN"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "TRUE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "IMPLIES",
            [
              "IMPLIES",
              "VAR_P",
              "VAR_Q"
            ],
            "VAR_R"
          ],
          "VAR_S"
        ]
      ]
    },
    {
      "line": 6,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "TRUE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "OR",
            [
              "AND",
              "VAR_P",
              [
                "NOT",
                "VAR_Q"
              ]
            ],
            "VAR_R"
          ],
          "VAR_S"
        ]
      ]
    },
    {
      "line": 6,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 5,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R",
          "VAR_S"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_S": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 6,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 33
```plaintext
let p = T
let q = T
let r = F
let x = ((p AND (NOT r)) OR (q AND r))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_R",
        "R_PAREN",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "VAR_Q",
        "AND",
        "VAR_R",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            "VAR_P",
            [
              "NOT",
              "VAR_R"
            ]
          ],
          [
            "AND",
            "VAR_Q",
            "VAR_R"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "FALSE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            "VAR_P",
            [
              "NOT",
              "VAR_R"
            ]
          ],
          [
            "AND",
            "VAR_Q",
            "VAR_R"
          ]
        ]
      ]
    },
    {
      "line": 5,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "TRUE",
      "VAR_R": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 5,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 34
```plaintext
let p = T
let x = (p AND T)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "TRUE",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "TRUE"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 35
```plaintext
let p = F
let x = (F OR p)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "FALSE",
        "OR",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "FALSE",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "FALSE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 36
```plaintext
let p = T
let x = (p AND F)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "FALSE",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "FALSE"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 37
```plaintext
let p = F
let x = (p OR T)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "OR",
        "TRUE",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "VAR_P",
          "TRUE"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 38
```plaintext
let p = T
let x = (p AND p)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 39
```plaintext
let p = T
let x = (p OR p)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "VAR_P",
          "VAR_P"
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 40
```plaintext
let p = T
let x = (p AND (NOT p))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          [
            "NOT",
            "VAR_P"
          ]
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 41
```plaintext
let p = T
let x = (p OR (NOT p))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "OR",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "VAR_P",
          [
            "NOT",
            "VAR_P"
          ]
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "TRUE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 42
```plaintext
let p = T
let q = F
let x = (p AND (p OR q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 43
```plaintext
let p = T
let q = F
let x = (p OR (p AND q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "OR",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          "VAR_P",
          [
            "AND",
            "VAR_P",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 44
```plaintext
let x = (NOT T)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "TRUE",
        "R_PAREN"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "TRUE"
        ]
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        "FALSE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 1,
        "variables_tested": [],
        "ast_original_column": [
          "FALSE"
        ],
        "ast_optimized_column": [
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 2,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 45
```plaintext
let x = (NOT F)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "FALSE",
        "R_PAREN"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          "FALSE"
        ]
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 1,
        "variables_tested": [],
        "ast_original_column": [
          "TRUE"
        ],
        "ast_optimized_column": [
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 2,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 46
```plaintext
let p = T
let x = (NOT (NOT p))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "NOT",
        "VAR_P",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          [
            "NOT",
            "VAR_P"
          ]
        ]
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 3,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 2,
        "variables_tested": [
          "VAR_P"
        ],
        "ast_original_column": [
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 3,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 47
```plaintext
let p = T
let q = F
let x = (NOT (p AND q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          [
            "AND",
            "VAR_P",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "NOT",
            "VAR_P"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 48
```plaintext
let p = T
let q = F
let x = (NOT (p OR q))
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "NOT",
          [
            "OR",
            "VAR_P",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          [
            "NOT",
            "VAR_P"
          ],
          [
            "NOT",
            "VAR_Q"
          ]
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "FALSE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "FALSE"
      }
    ]
  }
}
```

### Valid 49
```plaintext
let p = T
let q = F
let x = ((p AND q) OR p)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "OR",
        "VAR_P",
        "R_PAREN"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        [
          "OR",
          [
            "AND",
            "VAR_P",
            "VAR_Q"
          ],
          "VAR_P"
        ]
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_P"
      ]
    },
    {
      "line": 4,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 3,
        "variables_tested": [
          "VAR_P",
          "VAR_Q"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "FALSE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": [
      {
        "line": 4,
        "output": "TRUE"
      }
    ]
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_S",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_T",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "LET",
        "VAR_U",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 7,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "VAR_R",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_S",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "VAR_T",
        "OR",
        "VAR_U",
        "R_PAREN",
        "R_PAREN",
        "AND",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "VAR_P",
        "IMPLIES",
        "VAR_R",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN"
      ]
    },
    {
      "line": 8,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 7
  }
}
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
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_A",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_B",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_C",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_D",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "LET",
        "VAR_E",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "tokens": [
        "LET",
        "VAR_F",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 7,
      "tokens": [
        "IF",
        "L_PAREN",
        "L_PAREN",
        "L_PAREN",
        "VAR_A",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_B",
        "R_PAREN",
        "R_PAREN",
        "OR",
        "L_PAREN",
        "L_PAREN",
        "VAR_C",
        "IMPLIES",
        "VAR_D",
        "R_PAREN",
        "AND",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "VAR_E",
        "OR",
        "VAR_F",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "VAR_A",
        "OR",
        "VAR_C",
        "R_PAREN",
        "R_PAREN",
        "THEN",
        "PRINT",
        "VAR_A"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_A",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_B",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_C",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_D",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_E",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "ast": [
        "LET",
        "VAR_F",
        "FALSE"
      ]
    },
    {
      "line": 7,
      "ast": [
        "IF",
        [
          "IMPLIES",
          [
            "OR",
            [
              "AND",
              "VAR_A",
              [
                "NOT",
                "VAR_B"
              ]
            ],
            [
              "AND",
              [
                "IMPLIES",
                "VAR_C",
                "VAR_D"
              ],
              [
                "NOT",
                [
                  "OR",
                  "VAR_E",
                  "VAR_F"
                ]
              ]
            ]
          ],
          [
            "OR",
            "VAR_A",
            "VAR_C"
          ]
        ],
        [
          "PRINT",
          "VAR_A"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_A",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_B",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_C",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_D",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "LET",
        "VAR_E",
        "TRUE"
      ]
    },
    {
      "line": 6,
      "ast": [
        "LET",
        "VAR_F",
        "FALSE"
      ]
    },
    {
      "line": 7,
      "ast": [
        "IF",
        [
          "OR",
          [
            "AND",
            [
              "OR",
              [
                "NOT",
                "VAR_A"
              ],
              "VAR_B"
            ],
            [
              "OR",
              [
                "AND",
                "VAR_C",
                [
                  "NOT",
                  "VAR_D"
                ]
              ],
              [
                "OR",
                "VAR_E",
                "VAR_F"
              ]
            ]
          ],
          [
            "OR",
            "VAR_A",
            "VAR_C"
          ]
        ],
        [
          "PRINT",
          "VAR_A"
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 7,
        "variables_tested": [
          "VAR_A",
          "VAR_B",
          "VAR_C",
          "VAR_D",
          "VAR_E",
          "VAR_F"
        ],
        "ast_original_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE"
        ],
        "ast_optimized_column": [
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_A": "TRUE",
      "VAR_B": "FALSE",
      "VAR_C": "TRUE",
      "VAR_D": "FALSE",
      "VAR_E": "TRUE",
      "VAR_F": "FALSE"
    },
    "printed_output": [
      {
        "line": 7,
        "output": "TRUE"
      }
    ]
  }
}
```

### Valid 52
```plaintext
let p = T
let q = F
let r = T
let s = F
if (NOT ((NOT ((p OR q) IMPLIES (r AND (NOT s)))) AND (p IMPLIES (q OR r)))) then let x = (NOT (p AND s))
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "LET",
        "VAR_Q",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "tokens": [
        "LET",
        "VAR_R",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "tokens": [
        "LET",
        "VAR_S",
        "EQ",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "tokens": [
        "IF",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "OR",
        "VAR_Q",
        "R_PAREN",
        "IMPLIES",
        "L_PAREN",
        "VAR_R",
        "AND",
        "L_PAREN",
        "NOT",
        "VAR_S",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "AND",
        "L_PAREN",
        "VAR_P",
        "IMPLIES",
        "L_PAREN",
        "VAR_Q",
        "OR",
        "VAR_R",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "R_PAREN",
        "THEN",
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "NOT",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_S",
        "R_PAREN",
        "R_PAREN"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "IF",
        [
          "NOT",
          [
            "AND",
            [
              "NOT",
              [
                "IMPLIES",
                [
                  "OR",
                  "VAR_P",
                  "VAR_Q"
                ],
                [
                  "AND",
                  "VAR_R",
                  [
                    "NOT",
                    "VAR_S"
                  ]
                ]
              ]
            ],
            [
              "IMPLIES",
              "VAR_P",
              [
                "OR",
                "VAR_Q",
                "VAR_R"
              ]
            ]
          ]
        ],
        [
          "LET",
          "VAR_X",
          [
            "NOT",
            [
              "AND",
              "VAR_P",
              "VAR_S"
            ]
          ]
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "ast": [
        "LET",
        "VAR_Q",
        "FALSE"
      ]
    },
    {
      "line": 3,
      "ast": [
        "LET",
        "VAR_R",
        "TRUE"
      ]
    },
    {
      "line": 4,
      "ast": [
        "LET",
        "VAR_S",
        "FALSE"
      ]
    },
    {
      "line": 5,
      "ast": [
        "IF",
        [
          "OR",
          [
            "OR",
            [
              "AND",
              [
                "NOT",
                "VAR_P"
              ],
              [
                "NOT",
                "VAR_Q"
              ]
            ],
            [
              "AND",
              "VAR_R",
              [
                "NOT",
                "VAR_S"
              ]
            ]
          ],
          [
            "AND",
            "VAR_P",
            [
              "AND",
              [
                "NOT",
                "VAR_Q"
              ],
              [
                "NOT",
                "VAR_R"
              ]
            ]
          ]
        ],
        [
          "LET",
          "VAR_X",
          [
            "OR",
            [
              "NOT",
              "VAR_P"
            ],
            [
              "NOT",
              "VAR_S"
            ]
          ]
        ]
      ]
    }
  ],
  "phase_4_execution": {
    "verifications": [
      {
        "line": 5,
        "variables_tested": [
          "VAR_P",
          "VAR_Q",
          "VAR_R",
          "VAR_S"
        ],
        "ast_original_column": [
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "FALSE",
          "TRUE",
          "FALSE",
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      },
      {
        "line": 5,
        "variables_tested": [
          "VAR_P",
          "VAR_S"
        ],
        "ast_original_column": [
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "ast_optimized_column": [
          "FALSE",
          "TRUE",
          "TRUE",
          "TRUE"
        ],
        "is_equivalent": "TRUE"
      }
    ],
    "final_state_dictionary": {
      "VAR_P": "TRUE",
      "VAR_Q": "FALSE",
      "VAR_R": "TRUE",
      "VAR_S": "FALSE",
      "VAR_X": "TRUE"
    },
    "printed_output": []
  }
}
```

### Invalid L1
```plaintext
assign p = T
```
```json
{
  "error": {
    "phase": "phase_1_lexer",
    "line": 1
  }
}
```

### Invalid L2
```plaintext
let P = T
```
```json
{
  "error": {
    "phase": "phase_1_lexer",
    "line": 1
  }
}
```

### Invalid L3
```plaintext
let pp = T
```
```json
{
  "error": {
    "phase": "phase_1_lexer",
    "line": 1
  }
}
```

### Invalid L4
```plaintext
let x = (p and q)
```
```json
{
  "error": {
    "phase": "phase_1_lexer",
    "line": 1
  }
}
```

### Invalid L5
```plaintext
let p := T
```
```json
{
  "error": {
    "phase": "phase_1_lexer",
    "line": 1
  }
}
```

### Invalid L6
```plaintext
let x = (p XOR q)
```
```json
{
  "error": {
    "phase": "phase_1_lexer",
    "line": 1
  }
}
```

### Invalid S1
```plaintext
let p = T
if (p AND ) then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "TRUE"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "IF",
        "L_PAREN",
        "VAR_P",
        "AND",
        "R_PAREN",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 2
  }
}
```

### Invalid S2
```plaintext
let x = (p AND)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S3
```plaintext
let x = (AND p q)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "AND",
        "VAR_P",
        "VAR_Q",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S4
```plaintext
if p print q
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "IF",
        "VAR_P",
        "PRINT",
        "VAR_Q"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S5
```plaintext
let p =
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S6
```plaintext
print (p AND q)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "PRINT",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S7
```plaintext
let x = (p AND q) IMPLIES r
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "IMPLIES",
        "VAR_R"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S8
```plaintext
let x = ((p AND q)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S9
```plaintext
let x = (p AND q))
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S10
```plaintext
let x = ()
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S11
```plaintext
let x = (p)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S12
```plaintext
let x = ((p))
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "L_PAREN",
        "VAR_P",
        "R_PAREN",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S13
```plaintext
if p then if q print r
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "IF",
        "VAR_P",
        "THEN",
        "IF",
        "VAR_Q",
        "PRINT",
        "VAR_R"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S14
```plaintext
if p then then q
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "IF",
        "VAR_P",
        "THEN",
        "THEN",
        "VAR_Q"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S15
```plaintext
if then print p
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "IF",
        "THEN",
        "PRINT",
        "VAR_P"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S16
```plaintext
let p (NOT q)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "L_PAREN",
        "NOT",
        "VAR_Q",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S17
```plaintext
let x = p AND q
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "VAR_P",
        "AND",
        "VAR_Q"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid S18
```plaintext
let x = (AND OR NOT)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "AND",
        "OR",
        "NOT",
        "R_PAREN"
      ]
    }
  ],
  "error": {
    "phase": "phase_2_parser",
    "line": 1
  }
}
```

### Invalid E1
```plaintext
let p = t
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_P",
        "EQ",
        "VAR_T"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "VAR_T"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_P",
        "VAR_T"
      ]
    }
  ],
  "error": {
    "phase": "phase_4_execution",
    "line": 1
  }
}
```

### Invalid E2
```plaintext
let x = (p AND q)
print x
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_P",
        "AND",
        "VAR_Q",
        "R_PAREN"
      ]
    },
    {
      "line": 2,
      "tokens": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_P",
          "VAR_Q"
        ]
      ]
    },
    {
      "line": 2,
      "ast": [
        "PRINT",
        "VAR_X"
      ]
    }
  ],
  "error": {
    "phase": "phase_4_execution",
    "line": 1
  }
}
```

### Invalid E3
```plaintext
let x = (x AND T)
```
```json
{
  "phase_1_lexer": [
    {
      "line": 1,
      "tokens": [
        "LET",
        "VAR_X",
        "EQ",
        "L_PAREN",
        "VAR_X",
        "AND",
        "TRUE",
        "R_PAREN"
      ]
    }
  ],
  "phase_2_parser": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        [
          "AND",
          "VAR_X",
          "TRUE"
        ]
      ]
    }
  ],
  "phase_3_optimizer": [
    {
      "line": 1,
      "ast": [
        "LET",
        "VAR_X",
        "VAR_X"
      ]
    }
  ],
  "error": {
    "phase": "phase_4_execution",
    "line": 1
  }
}
```

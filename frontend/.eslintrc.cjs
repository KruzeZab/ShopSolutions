module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    "standard-with-typescript",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:jsx-a11y/recommended",
    "prettier",
  ],
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
    project: ["./tsconfig.json"],
  },
  plugins: ["jsx-a11y", "react"],
  rules: {
    "react/react-in-jsx-scope": "off",
    "@typescript-eslint/explicit-function-return-type": "off",
    "@typescript-eslint/triple-slash-reference": "off",
    "@typescript-eslint/strict-boolean-expressions": "off",
    "@typescript-eslint/no-floating-promises": "off",
    "@typescript-eslint/prefer-optional-chain": "off",

    "@typescript-eslint/no-misused-promises": [
      "error",
      {
        checksVoidReturn: false,
      },
    ],

    "import/order": [
      "error",
      {
        groups: ["builtin", "external", "parent", "sibling", "index"],
      },
    ],
  },
  settings: {
    react: {
      version: "detect",
    },
  },
};

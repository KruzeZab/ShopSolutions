module.exports = {
  extends: ["stylelint-config-standard", "stylelint-config-prettier"],
  overrides: [
    {
      files: ["**/*.{js,jsx,ts,tsx}"],
      customSyntax: "postcss-jsx",
    },
  ],
  rules: {
    "function-no-unknown": null,
    "selector-class-pattern": null,
    "value-keyword-case": [
      "lower",
      {
        ignoreKeywords: ["/theme.*/"],
      },
    ],
  },
};

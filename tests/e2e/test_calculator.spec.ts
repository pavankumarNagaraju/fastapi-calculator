import { test, expect } from "@playwright/test";

test("UI add flow", async ({ page }) => {
  await page.goto("http://127.0.0.1:8000/");
  await page.fill("#a", "10");
  await page.fill("#b", "7");
  await page.selectOption("#op", "add");
  await page.click("#calc");
  await expect(page.locator("#out")).toHaveText("17");
});

test("UI power flow", async ({ page }) => {
  await page.goto("http://127.0.0.1:8000/");
  await page.fill("#a", "2");
  await page.fill("#b", "5");
  await page.selectOption("#op", "power");
  await page.click("#calc");
  await expect(page.locator("#out")).toHaveText("32");
});

test("UI divide by zero shows error", async ({ page }) => {
  await page.goto("http://127.0.0.1:8000/");
  await page.fill("#a", "1");
  await page.fill("#b", "0");
  await page.selectOption("#op", "divide");
  await page.click("#calc");
  await expect(page.locator("#out")).toHaveText("Division by zero");
});

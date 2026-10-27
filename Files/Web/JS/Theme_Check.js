const ThemePreference = window.matchMedia("(prefers-color-scheme: dark)")
const ThemeToggle = document.getElementById("Theme_Toggle")
let HasManualTheme = false

function UpdateThemeToggle() {
    const Theme = document.documentElement.dataset.theme
    ThemeToggle.textContent = Theme === "dark" ? "Switch to light theme" : "Switch to dark theme"
}

function SetTheme(Theme) {
    document.documentElement.dataset.theme = Theme
    UpdateThemeToggle()
}

SetTheme(ThemePreference.matches ? "dark" : "light")

ThemePreference.addEventListener("change", () => {
    if (!HasManualTheme) {
        SetTheme(ThemePreference.matches ? "dark" : "light")
    }
})

ThemeToggle.addEventListener("click", () => {
    HasManualTheme = true
    SetTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark")
})

// Quartz v5 requires this module to export CustomOgImagesEmitterName.
// MoonDAO uses a static OG image (quartz/static/og-image.png) rather than
// a custom OG image emitter, so this exports the sentinel value and
// no emitter will be registered under this name.
export const CustomOgImagesEmitterName = "CustomOgImages"

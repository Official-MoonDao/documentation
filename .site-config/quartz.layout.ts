import { PageLayout, SharedLayout } from "./quartz/cfg";
import * as Component from "./quartz/components";

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/Official-MoonDao",
      "Discord Community": "https://discord.gg/moondao",
    },
  }),
};

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
    Component.TableOfContents(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(
      Component.Explorer({
        filterFn: (node) => {
          // set containing names of folders to filter out from sidebar
          const omit = new Set(["reference"]);
          return !omit.has(node.name.toLowerCase());
        },
      })
    ),
  ],
  right: [
    Component.MobileOnly(
      Component.Explorer({
        filterFn: (node) => {
          // set containing names of folders to filter out from sidebar
          const omit = new Set(["reference"]);
          return !omit.has(node.name.toLowerCase());
        },
      })
    ),
    Component.Graph(),
    Component.Backlinks(),
  ],
};

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [],
};

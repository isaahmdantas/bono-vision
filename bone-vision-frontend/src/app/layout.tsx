import type { Metadata } from "next";

import { fonts } from './fonts'
import "./globals.css";

import { Providers } from "./providers";


export const metadata: Metadata = {
  title: "Bone Vision",
  description: "This repository contains dashboards and reports with data related to osteoporosis risk prediction.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en' className={fonts.rubik.variable}>
      <body>  
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
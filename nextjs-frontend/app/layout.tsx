import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { ClerkProvider } from '@clerk/nextjs'

import { ToasterProvider } from '@/providers/toast-provider'

import './globals.css'
import { ThemeProvider } from '@/providers/theme-provider'
import { Suspense } from 'react'
import Loading from './loading'

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});



export const metadata: Metadata = {
  title: 'Uwezo Platform',
  description: 'An accountability platform for corruption, injustice, and abuse of power.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
          <ThemeProvider 
            attribute="class" 
            enableColorScheme
            defaultTheme="dark"
            enableSystem
            disableTransitionOnChange
          >
            <ToasterProvider />
            <Suspense fallback={ <Loading /> }>
              {children}
            </Suspense>
          </ThemeProvider>
        </body>
      </html>
    </ClerkProvider>
  )
}

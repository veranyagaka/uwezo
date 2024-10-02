// this centers the sign-in and sign-up page all at once.
// it's an alternative for going to the specific pages and adding flexboxes on the pages

export default function AuthLayout({
    children
}: {
    children: React.ReactNode
}) {
    return (
        <div className="flex items-center justify-center h-full">
            {children}
        </div>
    )
}
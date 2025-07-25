import { agentPlaygroundFlagFrontend } from '@/flags';
import { isFlagEnabled } from '@/lib/feature-flags';
import { Metadata } from 'next';
import { redirect } from 'next/navigation';

export const metadata: Metadata = {
  title: 'Agent Conversation | Kortix Suni',
  description: 'Interactive agent conversation powered by Kortix Suni',
  openGraph: {
    title: 'Agent Conversation | Kortix Suni',
    description: 'Interactive agent conversation powered by Kortix Suni',
    type: 'website',
  },
};

export default async function AgentsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}

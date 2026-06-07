import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const postsCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    author: z.string(),
    description: z.string(),
    tags: z.array(z.string()).optional(),
    tag: z.string().optional(),
    image: z.string().optional(),
  }),
});

export const collections = {
  posts: postsCollection,
};

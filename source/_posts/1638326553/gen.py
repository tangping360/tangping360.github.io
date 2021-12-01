for i in range(20):
  with open(f'Post{i:02}.md','wt',newline='\n') as fout:
    fout.write(f'---\n')
    fout.write(f'title: Post {i:02}\n')
    fout.write(f'date: 2021-11-{i:02} 00:00:00\n')
    fout.write(f'tag: GenPy\n')
    fout.write(f'---\n')
    fout.write(f'content {i:02} {i:02} {i:02}\n')

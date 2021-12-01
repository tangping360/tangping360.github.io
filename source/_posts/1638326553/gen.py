for i in range(20):
  with open(f'Post{i:02}.md','wt') as fout:
    fout.write(f'---\n')
    fout.write(f'title: Post{i:02}\n')
    fout.write(f'date: 2021-12-02 00:{i:02}:00\n')
    fout.write(f'---\n')
    fout.write(f'content {i:02} {i:02} {i:02}\n')

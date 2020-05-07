const fs = require('fs')

const data = JSON
  .parse(fs.readFileSync(process.argv[2]))
  .map((project) => ({
    cover: project.covers.original,
    createdAt: project.created_on,
    description: project.description,
    modules: project.modules.map((module) => {
      const m = { type: module.type }
      if (m.type === 'text') {
        m.text = module.text_plain
      } else if (m.type === 'image') {
        m.imageUrl = module.sizes.original
      } else {
        return module
      }

      return m
    }),
    name: project.name,
    stats: project.stats,
    tags: project.tags.map((tag) => tag.title),
    url: project.url
  }))

console.log(data)

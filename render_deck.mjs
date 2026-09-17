import fs from 'node:fs/promises';
import path from 'node:path';
import { FileBlob, PresentationFile } from '@oai/artifact-tool';
const input = path.join(process.cwd(),'deliverables','VenueFit_Boston_Presentation.pptx');
const out = path.join(process.cwd(),'.deck_preview');
await fs.mkdir(out,{recursive:true});
const deck = await PresentationFile.importPptx(await FileBlob.load(input));
for (let i=0;i<deck.slides.items.length;i++) {
  const img = await deck.slides.items[i].export({format:'png',scale:1});
  await fs.writeFile(path.join(out,`slide-${i+1}.png`),new Uint8Array(await img.arrayBuffer()));
}
console.log(out);

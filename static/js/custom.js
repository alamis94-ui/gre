// highlight when running on localhost or test site
window.onload = (e) => {
    let server
    if (location.hostname == 'localhost') {
        server = 'localhost'
    }
    let m = location.pathname.match(`^/(test-\\w+)/`)
    if (m)  {
        server = m[1]
    }
    if (server) {
        document.querySelector('body').classList.add(server)
        let div = document.createElement('div')
        div.classList.add('test-header')
        div.innerText = server
        document.querySelector('body').prepend(div)
    }
}
function fullscreen(img) {
    let d = document.querySelector('.fullscreen')
    if (d) {
        d.remove()
    }
    d = document.createElement('div')
    d.classList.add('fullscreen')
    d.style.backgroundImage = `url(${img.src})`
    d.style.display = 'block'
    document.querySelector('body').append(d)
    d.addEventListener('click', (x) => {
        d.remove()
    })
}

async function citeThis(e) {
    try {
        const citation = document.querySelector('cite').innerText
        const clip = new ClipboardItem({ ["text/plain"]: citation })
        await navigator.clipboard.write([clip])
        alert("This citation has been copied to your clipboard:\n\n" + citation)
    }
    catch (error) {
        alert("Sorry, there was an error when generating the citation.")
        console.log(error)
    }
}

function detectGreek() {
    document.querySelectorAll('em').forEach((em) => {
        let t = em.innerText
        for (let i=0; i < t.length; i++) {
            let c = t.codePointAt(i)
            // check if within "Greek and Coptic" or "Greek Extended" Unicode ranges
            if (c>=0x370 && c<=0x3ff || c>=0x1f00 && c<0x1fff){
                em.lang = 'el'
                break
            }
        }
    })
}

function detectGreek2() {
    let m = document.querySelector('.main .content')
    let els = m.getElementsByTagName('*')
    for (let i=0; i<els.length; i++) {
        let nodes = els.item(i).childNodes
        for (let j=0; j<nodes.length; j++) {
            let n = nodes[j]
            if (n.nodeType==3) {
                let words = n.nodeValue.split(" ")
                let words2 = []
                let greek = false
                for (let wi=0; wi<words.length; wi++) {
                    let w = words[wi]
                    if (w.match(/[\u0370-\u03ff\u1f00-\u1fff]/)) {
                        words2.push("<em lang='el'>" + w + "</em>")
                        greek = true
                    }
                    else {
                        words2.push(w)
                    }
                }
                if (greek) {
                    n.nodeValue = words2.join(" ")
                }
            }
        }
    }
}

detectGreek()
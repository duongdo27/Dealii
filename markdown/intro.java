/*! class B */
class B {};
/*! class C */
class C {};
/*! \mainpage
  
 *  Class relations expressed via an inline dot graph:
 *  \dot
 *  digraph example {
 *      node [shape=record, fontname=Helvetica, fontsize=10];
 *      b [ label="class B" URL="\ref B"];
 *      c [ label="class C" URL="\ref C"];
 *      b -> c [ arrowhead="open", style="dashed" ];
 *  }
 *  \enddot
 *  Note that the classes in the above graph are clickable
 *  (in the HTML output).
 *	\dotfile grap2.dot
 */
 